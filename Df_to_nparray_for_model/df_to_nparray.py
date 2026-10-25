import numpy as np
import pandas as pd
import logging
import argparse
from pathlib import Path
import sys

log = logging.getLogger(__name__)

def logging_setup() -> None:
    
    logging.basicConfig(
        level= logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
        handlers= [
            # logging.FileHandler('Logs_of_DF_to_NP.log'),
            logging.StreamHandler()
        ],
        
        force= True
    )

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description = 'Converting dataset to Numpy Array',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    ) 
    
    parser.add_argument(
        '--input',
        type = Path,
        required = True,
        help = "Path to the dataset"
    )
    
    parser.add_argument(
        '--output',
        type = Path,
        required = True,
        help = 'Path to store the result'
    )

    return parser.parse_args()

REQUIRED = ["temperature","pressure", "humidity"]

def df_to_np(input: Path, output: Path) -> np.ndarray:

    try:
        df = pd.read_csv(input)
        log.info("Loaded a dataset shaped: %s", df.shape)
    except FileNotFoundError as fnfe:
        log.error("File not founded: %s", fnfe)
        sys.exit(1)

    
    missing = [col for col in REQUIRED if col not in df.columns]

    if not missing:

        log.info("Required column are present in the Dataset.")
        df = df[REQUIRED]
        log.info("Selected feature columns %s in model order, Shape: %s", REQUIRED, df.shape)

        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        nan_col = df.isna().any(axis=0)
        nan_col = df.columns[nan_col].tolist()

        if nan_col:
            log.error("Missing or Non-numeric values in:: %s", nan_col)
            sys.exit(1)
    else:
        log.error("Missing columns: %s, Exiting the script.", missing)
        sys.exit(1)

    arr = df.to_numpy(dtype="float32")
    log.info("Converted the DataFrame to np.array")

    try:
        np.save(output, arr)
        log.info("Saved array to %s with shape %s and dtype is %s and byte-size is %s", output, arr.shape, arr.dtype, arr.nbytes)
    except Exception as e:
        log.error("Failed to save file: %s", e)
        sys.exit(1)

    return arr      

if __name__ == "__main__":
    logging_setup()
    args = arg_parser()
    df_to_np(input=args.input, output=args.output)

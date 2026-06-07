from manim import *
import random
import numpy as np

class ShapesDemo(Scene):
    def construct(self):
        circle = Circle(radius=1)       # Create a circle
        square = Square(side_length=2)  # Create a square

        square.next_to(circle, RIGHT)   # Position square to the right of the circle

        self.play(Create(circle))       # Animate circle creation
        self.play(Create(square))       # Animate square creation
        self.wait(1)

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Arsalan!")
        self.play(Write(text))

class ChileInflation(Scene):
    def construct(self):
        # 1. SETUP THE AXES (Disable automatic LaTeX numbers)
        axes = Axes(
            x_range=[1970, 1974, 1],       # Years 1970 to 1973
            y_range=[0, 700, 100],         # Inflation 0% to 600%
            x_length=8,
            y_length=5,
            axis_config={
                "color": GREY_B, 
                "include_numbers": False,  # <--- CRITICAL FIX: Turn off LaTeX numbers
                "tip_shape": StealthTip,
            },
        ).to_edge(DOWN)

        # 2. MANUALLY ADD LABELS (Using 'Text' engine, not LaTeX)
        
        # Add X-Axis Numbers (Years)
        x_labels = VGroup()
        for year in range(1970, 1974):
            # Position text manually below the tick mark
            lab = Text(str(year), font_size=20, font="Arial").next_to(axes.c2p(year, 0), DOWN)
            x_labels.add(lab)

        # Add Y-Axis Numbers (Inflation %)
        y_labels = VGroup()
        for value in range(0, 700, 100):
            # Position text manually to the left
            lab = Text(str(value), font_size=20, font="Arial").next_to(axes.c2p(1970, value), LEFT)
            y_labels.add(lab)

        # Main Axis Titles
        x_title = Text("Year", font_size=24).next_to(axes.x_axis, DOWN * 2)
        y_title = Text("Inflation (%)", font_size=24).next_to(axes.y_axis, UP)

        # 3. DATA PLOTTING
        # Segment 1: The "Normal" Years (White Line)
        graph_1 = axes.plot_line_graph(
            x_values=[1970, 1971],
            y_values=[36, 22],
            line_color=WHITE,
            add_vertex_dots=True,
        )

        # Segment 2: The "Crisis" Begins (Yellow Line)
        graph_2 = axes.plot_line_graph(
            x_values=[1971, 1972],
            y_values=[22, 260],
            line_color=YELLOW,
            add_vertex_dots=True,
        )

        # Segment 3: The "Collapse" (Red Line - Vertical Spike)
        graph_3 = axes.plot_line_graph(
            x_values=[1972, 1973],
            y_values=[260, 608],
            line_color=RED,
            stroke_width=6,
            add_vertex_dots=True,
        )

        # 4. ANIMATION SEQUENCE
        # Draw axes and manual labels
        self.play(
            Create(axes), 
            Write(x_labels), 
            Write(y_labels), 
            Write(x_title), 
            Write(y_title), 
            run_time=2
        )
        
        # 1970-1971 (Steady)
        self.play(Create(graph_1), run_time=2, rate_func=linear)
        self.wait(0.5)
        
        # 1971-1972 (Speeding up)
        self.play(Create(graph_2), run_time=1.5, rate_func=smooth)
        
        # 1972-1973 (The Explosion)
        self.play(Create(graph_3), run_time=0.8, rate_func=rush_from)
        
        # Add a "600%" Label at the top
        final_value = Text("600%+", color=RED, font_size=48).move_to(axes.c2p(1973, 650))
        self.play(Write(final_value), Flash(final_value))

        self.wait(2)

class CopperDrainTape(Scene):
    def construct(self):
        # --- PALETTE ---
        BLOOD_MAP_FILL = "#720e1e"   
        BLOOD_MAP_STROKE = "#3b070f"
        
        # LABEL COLORS
        TAPE_BLACK = "#000000"       # The box background
        TEXT_WHITE = "#FFFFFF"       # The text color
        BORDER_RED = "#FF0000"       # The "Danger" border
        COPPER_ACCENT = "#ffb347"    

        # FONT: Back to Courier (The "File" look)
        FONT = "Courier New"         

        # 1. THE BLOOD MAP
        chile_map = SVGMobject("chile.svg")
        chile_map.height = 6.5
        chile_map.move_to(ORIGIN)
        chile_map.set_fill(color=BLOOD_MAP_FILL, opacity=1) 
        chile_map.set_stroke(color=BLOOD_MAP_STROKE, width=2)

        # 2. LOCATIONS
        mine_1_pos = [-0.1, 1.8, 0] 
        mine_2_pos = [-0.2, -0.2, 0]

        mine_1 = Dot(point=mine_1_pos, color=COPPER_ACCENT, radius=0.1)
        mine_2 = Dot(point=mine_2_pos, color=COPPER_ACCENT, radius=0.1)
        
        ring_1 = Circle(radius=0.2, color=COPPER_ACCENT, stroke_width=1.5).move_to(mine_1)
        ring_2 = Circle(radius=0.2, color=COPPER_ACCENT, stroke_width=1.5).move_to(mine_2)

        # 3. HELPER: The "Label Tape" Function
        def create_tape_label(text, font_size=24, border_color=None):
            # The Text
            t = Text(text, font=FONT, font_size=font_size, color=TEXT_WHITE, weight=BOLD)
            # The Box (Tape)
            bg = SurroundingRectangle(t, color=TAPE_BLACK, fill_color=TAPE_BLACK, fill_opacity=1, buff=0.15, corner_radius=0.05)
            # Optional Border
            if border_color:
                bg.set_stroke(color=border_color, width=3)
            else:
                bg.set_stroke(width=0)
            return VGroup(bg, t)

        # 4. CREATE LABELS
        # Mine Names (Small, Simple Tape)
        lbl_1 = create_tape_label("CHUQUICAMATA", font_size=16).next_to(mine_1, LEFT, buff=0.8)
        lbl_2 = create_tape_label("EL TENIENTE", font_size=16).next_to(mine_2, LEFT, buff=0.8)

        # Pointers
        ptr_1 = Line(lbl_1.get_right(), ring_1.get_left(), color=COPPER_ACCENT, stroke_width=1)
        ptr_2 = Line(lbl_2.get_right(), ring_2.get_left(), color=COPPER_ACCENT, stroke_width=1)

        # 5. THE VILLAINS (Big Tape with Red Border)
        # Header
        usa_text = create_tape_label("USA / CORPORATIONS", font_size=20)
        usa_text.move_to([4.5, 2.8, 0])
        
        # Companies
        corp_1 = create_tape_label("ANACONDA", font_size=32, border_color=BORDER_RED)
        corp_1.next_to(usa_text, DOWN, aligned_edge=RIGHT, buff=0.2)
        
        corp_2 = create_tape_label("KENNECOTT", font_size=32, border_color=BORDER_RED)
        corp_2.next_to(corp_1, DOWN, aligned_edge=RIGHT, buff=0.1)

        # 6. FLOW LINES
        line_1 = ArcBetweenPoints(start=mine_1.get_center(), end=usa_text.get_left(), angle=-TAU/8)
        line_2 = ArcBetweenPoints(start=mine_2.get_center(), end=usa_text.get_left(), angle=-TAU/8)
        
        dashed_1 = DashedVMobject(line_1.set_color(COPPER_ACCENT).set_stroke(width=3), num_dashes=25)
        dashed_2 = DashedVMobject(line_2.set_color(COPPER_ACCENT).set_stroke(width=3), num_dashes=30)

        # --- ANIMATION SEQUENCE ---
        
        # 1. Map
        self.play(DrawBorderThenFill(chile_map), run_time=2)
        
        # 2. Mines & Small Labels
        self.play(
            FadeIn(mine_1, scale=0.5), Create(ring_1),
            FadeIn(mine_2, scale=0.5), Create(ring_2),
        )
        self.play(
            FadeIn(lbl_1, shift=RIGHT), Create(ptr_1),
            FadeIn(lbl_2, shift=RIGHT), Create(ptr_2)
        )
        
        # 3. USA Header & Flow
        self.play(FadeIn(usa_text, shift=DOWN))
        self.play(Create(dashed_1), Create(dashed_2), run_time=1.5)
        
        # 4. THE SLAM (The Villains)
        # They grow from center, looking like they are being stamped on
        self.play(GrowFromCenter(corp_1), run_time=0.5)
        self.play(GrowFromCenter(corp_2), run_time=0.5)
        
        # 5. Pulse The Danger Border
        self.play(
            Indicate(corp_1[0], color=RED, scale_factor=1.05), # Index 0 is the box
            Indicate(corp_2[0], color=RED, scale_factor=1.05),
            run_time=1.5
        )
        
        self.wait(2)

class ElectionModern(Scene):
    def construct(self):
        # --- PALETTE (Modern & Sleek) ---
        ALLENDE_GRADIENT = [RED_D, RED_A] 
        OPPONENT_GRADIENT = [GREY_D, GREY_B] 
        
        TEXT_WHITE = "#FFFFFF"
        TEXT_GREY = "#AAAAAA" 
        
        MODERN_FONT = "Arial"

        # 1. SETUP DATA
        h_allende = 3.66 * 1.3
        h_alessandri = 3.53 * 1.3
        h_tomic = 2.78 * 1.3

        BAR_WIDTH = 0.7
        CORNER_RAD = 0.15

        # 2. BUILD THE BARS (Using RoundedRectangle)
        # FIX: Changed 'Rectangle' to 'RoundedRectangle' and passed corner_radius first
        
        # Allende (Center)
        bar_1 = RoundedRectangle(corner_radius=CORNER_RAD, height=h_allende, width=BAR_WIDTH)
        bar_1.set_fill(color=ALLENDE_GRADIENT, opacity=1)
        bar_1.set_stroke(width=0)
        
        # Alessandri (Right)
        bar_2 = RoundedRectangle(corner_radius=CORNER_RAD, height=h_alessandri, width=BAR_WIDTH)
        bar_2.set_fill(color=OPPONENT_GRADIENT, opacity=1)
        bar_2.set_stroke(width=0)

        # Tomic (Left)
        bar_3 = RoundedRectangle(corner_radius=CORNER_RAD, height=h_tomic, width=BAR_WIDTH)
        bar_3.set_fill(color=OPPONENT_GRADIENT, opacity=1)
        bar_3.set_stroke(width=0)
        
        # Align bottoms and space them out
        bar_group = VGroup(bar_3, bar_1, bar_2).arrange(RIGHT, buff=1.5, aligned_edge=DOWN)
        bar_group.move_to(DOWN * 0.5)

        # 3. LABELS
        name_1 = Text("Allende", font=MODERN_FONT, font_size=24, color=TEXT_WHITE).next_to(bar_1, DOWN, buff=0.3)
        name_2 = Text("Alessandri", font=MODERN_FONT, font_size=20, color=TEXT_GREY).next_to(bar_2, DOWN, buff=0.3)
        name_3 = Text("Tomic", font=MODERN_FONT, font_size=20, color=TEXT_GREY).next_to(bar_3, DOWN, buff=0.3)
        
        sub_1 = Text("(Marxist Candidate)", font=MODERN_FONT, font_size=16, color=RED_B).next_to(name_1, DOWN, buff=0.1)

        # 4. PERCENTAGES
        perc_1 = Text("36.6%", font=MODERN_FONT, font_size=48, color=TEXT_WHITE, weight=BOLD).next_to(bar_1, UP, buff=0.3)
        perc_2 = Text("35.3%", font=MODERN_FONT, font_size=32, color=TEXT_GREY).next_to(bar_2, UP, buff=0.3)
        perc_3 = Text("27.8%", font=MODERN_FONT, font_size=32, color=TEXT_GREY).next_to(bar_3, UP, buff=0.3)

        # --- ANIMATION ---
        
        # 1. Bars grow smoothly
        self.play(
            GrowFromEdge(bar_1, DOWN),
            GrowFromEdge(bar_2, DOWN),
            GrowFromEdge(bar_3, DOWN),
            run_time=1.5,
            rate_func=smooth 
        )
        
        # 2. Text fades in
        self.play(
            FadeIn(name_1, shift=UP), FadeIn(sub_1, shift=UP),
            FadeIn(name_2, shift=UP),
            FadeIn(name_3, shift=UP),
            FadeIn(perc_1, shift=DOWN),
            FadeIn(perc_2, shift=DOWN),
            FadeIn(perc_3, shift=DOWN),
            run_time=0.8
        )

        # 3. Highlight the gap
        self.play(
            bar_2.animate.set_opacity(0.7), perc_2.animate.set_opacity(0.7),
            bar_3.animate.set_opacity(0.7), perc_3.animate.set_opacity(0.7),
            bar_1.animate.set_stroke(color=WHITE, width=2, opacity=0.5),
            Indicate(perc_1, scale_factor=1.05, color=RED),
            run_time=1.5
        )
        
        self.wait(2)

class AssetsModern(Scene):
    def construct(self):
        # --- PALETTE ---
        MAP_COLOR = "#4A6572"        
        MAP_STROKE = "#90A4AE"
        TEXT_GREY = "#B0BEC5"
        MONEY_GREEN = "#69F0AE"      
        ACCENT_COPPER = "#FFAB91"    
        
        # Use a standard font available on Linux
        MODERN_FONT = "sans-serif" 

        # 1. THE MAP
        chile_map = SVGMobject("chile.svg")
        chile_map.height = 6.5
        chile_map.set_fill(color=MAP_COLOR, opacity=1)
        chile_map.set_stroke(color=MAP_STROKE, width=1.5)
        chile_map.move_to(LEFT * 2.5)

        # 2. THE MINES
        mine_1 = Dot(point=chile_map.get_center() + UP*1.8 + RIGHT*0.2, color=ACCENT_COPPER, radius=0.1)
        mine_2 = Dot(point=chile_map.get_center() + DOWN*0.2 + RIGHT*0.1, color=ACCENT_COPPER, radius=0.1)
        
        ring_1 = Circle(radius=0.2, color=ACCENT_COPPER, stroke_width=1).move_to(mine_1)
        ring_2 = Circle(radius=0.2, color=ACCENT_COPPER, stroke_width=1).move_to(mine_2)

        # 3. THE ASSET CARD
        card_bg = RoundedRectangle(corner_radius=0.2, height=3, width=5, color=GREY_D)
        card_bg.set_fill(color="#263238", opacity=0.9) 
        card_bg.set_stroke(color=TEXT_GREY, width=1)
        card_bg.move_to(RIGHT * 3)

        # 4. HEADER
        header = Text("TOTAL ASSET VALUATION", font=MODERN_FONT, font_size=24, color=TEXT_GREY, weight=BOLD)
        header.next_to(card_bg.get_top(), DOWN, buff=0.4)
        
        # 5. THE MANUAL COUNTER (Zero Dependencies)
        # We manually update a Text object to look like a counter
        val_tracker = ValueTracker(0)
        
        # This function creates the number text every frame
        def get_number_text():
            val = val_tracker.get_value()
            return Text(f"{val:.1f}", font=MODERN_FONT, font_size=80, color=MONEY_GREEN).move_to(card_bg.get_center())

        # Initial display
        number_display = get_number_text()
        
        currency_symbol = Text("$", font=MODERN_FONT, font_size=60, color=MONEY_GREEN)
        currency_symbol.next_to(number_display, LEFT, buff=0.1).shift(UP*0.1)
        
        unit_label = Text("BILLION", font=MODERN_FONT, font_size=30, color=MONEY_GREEN)
        unit_label.next_to(number_display, DOWN, buff=0.1)

        sub_text = Text("(Adjusted for Inflation)", font=MODERN_FONT, font_size=16, color=TEXT_GREY)
        sub_text.next_to(card_bg.get_bottom(), UP, buff=0.3)

        # 6. CONNECTING LINES
        line_1 = Line(mine_1.get_center(), card_bg.get_left(), color=TEXT_GREY, stroke_width=1).set_opacity(0.5)
        line_2 = Line(mine_2.get_center(), card_bg.get_left(), color=TEXT_GREY, stroke_width=1).set_opacity(0.5)

        # --- ANIMATION ---
        
        # 1. Draw Map
        self.play(DrawBorderThenFill(chile_map), run_time=1.5)
        self.play(
            FadeIn(mine_1), FadeIn(ring_1),
            FadeIn(mine_2), FadeIn(ring_2)
        )
        
        # 2. Show Card
        self.play(
            Create(line_1), Create(line_2),
            FadeIn(card_bg, shift=LEFT),
            run_time=1
        )
        self.play(Write(header))
        
        # 3. COUNT UP
        self.add(number_display, currency_symbol, unit_label)
        
        # The Updater logic
        def update_display(mob):
            new_mob = get_number_text()
            new_mob.move_to(mob)
            mob.become(new_mob)
            # Keep symbol attached
            currency_symbol.next_to(mob, LEFT, buff=0.1).shift(UP*0.1)
            
        number_display.add_updater(update_display)
        
        self.play(
            val_tracker.animate.set_value(7.4),
            run_time=2.5,
            rate_func=rate_functions.ease_out_expo
        )
        
        number_display.remove_updater(update_display)
        
        # 4. Final Pulse
        self.play(
            Indicate(number_display, color=MONEY_GREEN, scale_factor=1.1),
            Indicate(unit_label, color=MONEY_GREEN)
        )
        self.play(Write(sub_text))
        
        self.wait(2)

class ReformsModern(Scene):
    def construct(self):
        # --- PALETTE (Matches 'AssetsFinal') ---
        BG_COLOR = "#263238"    # Dark Blue-Grey (Card BG)
        TEXT_WHITE = "#FFFFFF"
        TEXT_GREY = "#B0BEC5"
        ACCENT_GREEN = "#69F0AE" # Growth/Social
        ACCENT_LAND = "#FFAB91"  # Land color
        
        MODERN_FONT = "sans-serif"

        # 1. TITLE
        title = Text("ALLENDE'S AGENDA", font=MODERN_FONT, font_size=36, color=TEXT_WHITE, weight=BOLD)
        title.to_edge(UP, buff=1)
        underline = Line(LEFT*3, RIGHT*3, color=TEXT_GREY).next_to(title, DOWN)

        # 2. LEFT CARD: LAND REFORM
        # Concept: A big square (Latifundia) splitting into 4 small squares
        card_land = RoundedRectangle(corner_radius=0.2, height=4, width=5, color=TEXT_GREY)
        card_land.set_fill(color=BG_COLOR, opacity=0.9)
        card_land.move_to(LEFT * 3 + DOWN * 0.5)
        
        lbl_land = Text("AGRARIAN REFORM", font=MODERN_FONT, font_size=20, color=ACCENT_LAND).next_to(card_land.get_top(), DOWN, buff=0.3)
        
        # The "Big Estate"
        big_square = Square(side_length=2, color=ACCENT_LAND, fill_opacity=0.5).move_to(card_land.get_center() + DOWN*0.3)
        
        # The "Distributed Land" (4 small squares)
        small_squares = VGroup(
            Square(side_length=0.9, color=ACCENT_LAND, fill_opacity=0.5),
            Square(side_length=0.9, color=ACCENT_LAND, fill_opacity=0.5),
            Square(side_length=0.9, color=ACCENT_LAND, fill_opacity=0.5),
            Square(side_length=0.9, color=ACCENT_LAND, fill_opacity=0.5)
        ).arrange_in_grid(2, 2, buff=0.1).move_to(big_square)

        # 3. RIGHT CARD: SOCIAL PROGRAMS
        # Concept: A checklist of benefits
        card_social = RoundedRectangle(corner_radius=0.2, height=4, width=5, color=TEXT_GREY)
        card_social.set_fill(color=BG_COLOR, opacity=0.9)
        card_social.move_to(RIGHT * 3 + DOWN * 0.5)
        
        lbl_social = Text("SOCIAL PROGRAMS", font=MODERN_FONT, font_size=20, color=ACCENT_GREEN).next_to(card_social.get_top(), DOWN, buff=0.3)
        
        # The List
        item_1 = Text("+ Free Milk (Children)", font=MODERN_FONT, font_size=18, color=TEXT_WHITE)
        item_2 = Text("+ Literacy Campaign", font=MODERN_FONT, font_size=18, color=TEXT_WHITE)
        item_3 = Text("+ Public Housing", font=MODERN_FONT, font_size=18, color=TEXT_WHITE)
        item_4 = Text("+ Wage Increases", font=MODERN_FONT, font_size=18, color=TEXT_WHITE)
        
        social_list = VGroup(item_1, item_2, item_3, item_4).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        social_list.move_to(card_social.get_center() + DOWN*0.2)

        # --- ANIMATION ---
        
        # 1. Setup
        self.play(Write(title), Create(underline))
        self.play(FadeIn(card_land, shift=RIGHT), FadeIn(card_social, shift=LEFT))
        self.play(Write(lbl_land), Write(lbl_social))
        
        # 2. Animate Land Reform (Split)
        self.play(DrawBorderThenFill(big_square))
        self.wait(0.3)
        self.play(
            ReplacementTransform(big_square, small_squares),
            run_time=1.5,
            rate_func=rate_functions.ease_out_back
        )
        
        # 3. Animate Social Programs (Checklist Pop)
        for item in social_list:
            self.play(
                FadeIn(item, shift=RIGHT),
                run_time=0.4
            )
        
        # 4. Final Pulse
        self.play(
            Indicate(small_squares, color=WHITE),
            Indicate(social_list, color=WHITE)
        )
        
        self.wait(2)

class SovietConquestArt(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        SOVIET_RED = "#D32F2F"
        HEAVY_FONT = "sans-serif"
        
        # 1. LOAD YOUR ARTWORK
        # Filename updated to remove spaces
        soviet_map = ImageMobject("SUART.png")
        soviet_map.scale_to_fit_height(7)
        soviet_map.move_to(LEFT * 3.5)
        
        # 2. TEXT & LAYOUT (Right Side)
        lbl_header = Text("GEOPOLITICAL THREAT", font=HEAVY_FONT, font_size=20, color=GRAY, weight=BOLD)
        lbl_header.move_to(RIGHT * 2 + UP * 2, aligned_edge=LEFT)

        lbl_title = Text("TOTAL SOVIET CONTROL", font=HEAVY_FONT, font_size=42, color=SOVIET_RED, weight=BOLD)
        lbl_title.next_to(lbl_header, DOWN, buff=0.2, aligned_edge=LEFT)

        # --- ANIMATION ---
        
        # A. Header fades in
        self.play(FadeIn(lbl_header, shift=RIGHT), run_time=1)

        # B. THE REVEAL (The "Stamp" Effect)
        self.play(
            ScaleInPlace(soviet_map, 0, rate_func=rate_functions.ease_out_elastic), 
            FadeIn(soviet_map),
            FadeIn(lbl_title, shift=LEFT),
            run_time=2
        )
        
        # C. The Pulse (Danger)
        self.play(
            Indicate(soviet_map, color=RED, scale_factor=1.05),
            Indicate(lbl_title, color=RED),
            run_time=1.5
        )
        
        self.wait(2)

class FinancialWipeoutFinal(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        TERMINAL_GREEN = "#00FF41"
        ALERT_RED = "#FF3333"
        TEXT_COLOR = "#E0E0E0"
        FONT = "Monospace"

        # --- 1. TRACKERS ---
        tracker_1 = ValueTracker(0)
        tracker_2 = ValueTracker(0)
        tracker_3 = ValueTracker(0)
        
        amt_1 = 234000000
        amt_2 = 150500000
        amt_3 = 85000000

        # --- 2. LAYOUT POSITIONS ---
        start_y = 1.5
        gap_y = 1.0
        
        label_x = -4
        val_x = 0
        stat_x = 4

        # --- ROW 1 ---
        lbl_1 = Text("US EX-IM BANK", font=FONT, font_size=24, color=TEXT_COLOR)
        lbl_1.move_to([label_x, start_y, 0]).align_to(LEFT * 4, LEFT)
        
        val_1 = always_redraw(lambda: 
            Text(f"{int(tracker_1.get_value()):,}", font=FONT, font_size=24, color=TERMINAL_GREEN)
            .move_to([val_x, start_y, 0])
            .align_to(RIGHT * 1.5, RIGHT)
        )
        
        status_1 = Text("[ ACTIVE ]", font=FONT, font_size=24, color=TERMINAL_GREEN).move_to([stat_x, start_y, 0])

        # --- ROW 2 ---
        lbl_2 = Text("WORLD BANK", font=FONT, font_size=24, color=TEXT_COLOR)
        lbl_2.move_to([label_x, start_y - gap_y, 0]).align_to(lbl_1, LEFT)
        
        val_2 = always_redraw(lambda: 
            Text(f"{int(tracker_2.get_value()):,}", font=FONT, font_size=24, color=TERMINAL_GREEN)
            .move_to([val_x, start_y - gap_y, 0])
            .align_to(val_1, RIGHT)
        )
        
        status_2 = Text("[ ACTIVE ]", font=FONT, font_size=24, color=TERMINAL_GREEN).move_to([stat_x, start_y - gap_y, 0])

        # --- ROW 3 ---
        lbl_3 = Text("IADB CREDIT", font=FONT, font_size=24, color=TEXT_COLOR)
        lbl_3.move_to([label_x, start_y - 2*gap_y, 0]).align_to(lbl_1, LEFT)
        
        val_3 = always_redraw(lambda: 
            Text(f"{int(tracker_3.get_value()):,}", font=FONT, font_size=24, color=TERMINAL_GREEN)
            .move_to([val_x, start_y - 2*gap_y, 0])
            .align_to(val_1, RIGHT)
        )
        
        status_3 = Text("[ ACTIVE ]", font=FONT, font_size=24, color=TERMINAL_GREEN).move_to([stat_x, start_y - 2*gap_y, 0])

        # --- HEADERS ---
        header_bank = Text("INSTITUTION", font=FONT, font_size=18, color=GRAY).next_to(lbl_1, UP, buff=0.5).align_to(lbl_1, LEFT)
        header_val = Text("LIQUIDITY ($)", font=FONT, font_size=18, color=GRAY).move_to([val_x, start_y + 0.8, 0])
        header_stat = Text("STATUS", font=FONT, font_size=18, color=GRAY).move_to([stat_x, start_y + 0.8, 0])
        
        divider = Line(LEFT*6, RIGHT*6, color=GRAY).next_to(header_bank, DOWN, buff=0.2)

        # --- 3. ANIMATION ---

        # A. Setup
        self.play(
            FadeIn(header_bank), FadeIn(header_val), FadeIn(header_stat),
            Create(divider),
            run_time=1
        )
        
        # B. Data Stream
        self.add(val_1, val_2, val_3)
        self.play(
            Write(lbl_1), Write(lbl_2), Write(lbl_3),
            FadeIn(status_1), FadeIn(status_2), FadeIn(status_3),
            tracker_1.animate.set_value(amt_1),
            tracker_2.animate.set_value(amt_2),
            tracker_3.animate.set_value(amt_3),
            run_time=2,
            rate_func=linear
        )
        self.wait(1)

        # C. THE WIPEOUT
        blocked_text = "[ FROZEN ]"
        
        self.play(
            Transform(status_1, Text(blocked_text, font=FONT, font_size=24, color=ALERT_RED).move_to(status_1)),
            Transform(status_2, Text(blocked_text, font=FONT, font_size=24, color=ALERT_RED).move_to(status_2)),
            Transform(status_3, Text(blocked_text, font=FONT, font_size=24, color=ALERT_RED).move_to(status_3)),
            tracker_1.animate.set_value(0),
            tracker_2.animate.set_value(0),
            tracker_3.animate.set_value(0),
            run_time=2.5,
            rate_func=linear
        )
        
        # --- D. ALERT OVERLAY (THE FIX) ---
        
        # 1. Create the Text FIRST
        alert_text = Text("AUTHORIZATION REVOKED", font="Impact", font_size=60, color=ALERT_RED)
        
        # 2. Create the Box BASED on the text size (buff adds padding)
        alert_box = SurroundingRectangle(alert_text, color=ALERT_RED, fill_color=BLACK, fill_opacity=0.9, buff=0.3, stroke_width=6)
        
        # 3. Group them
        alert_group = VGroup(alert_box, alert_text).move_to(ORIGIN)
        
        self.play(FadeIn(alert_group, scale=1.2), run_time=0.2)
        self.play(Wiggle(alert_group), run_time=0.5)
        
        self.wait(2)

class SupplyChainCollapse(Scene):
    def construct(self):
        # --- CONFIGURATION ---
        TERMINAL_GREEN = "#00FF41"
        ALERT_RED = "#FF3333"
        ROAD_GREY = "#333333"
        FONT = "Monospace"

        # --- 1. THE MAP (Abstract) ---
        # Chile is just a long vertical line in logistics terms
        highway = Line(UP*3.5, DOWN*3.5, color=ROAD_GREY, stroke_width=15)
        
        # Cities (Nodes)
        cities = VGroup()
        city_data = [
            ("ANTOFAGASTA", 2.5),
            ("VALPARAISO", 1.0),
            ("SANTIAGO", 0.0),
            ("CONCEPCION", -1.5),
            ("PUERTO MONTT", -3.0)
        ]
        
        for name, y_pos in city_data:
            # City Dot
            dot = Dot(point=UP*y_pos, color=WHITE, radius=0.12)
            # City Label
            label = Text(name, font=FONT, font_size=20, color=GRAY).next_to(dot, RIGHT, buff=0.4)
            # Status Indicator
            status = Text("SUPPLY: OK", font=FONT, font_size=16, color=TERMINAL_GREEN).next_to(label, DOWN, buff=0.1).align_to(label, LEFT)
            
            cities.add(VGroup(dot, label, status))

        # Title
        title = Text("NATIONAL LOGISTICS NETWORK", font=FONT, font_size=28, color=WHITE).to_corner(UL)
        
        # --- 2. THE FLOW (Traffic) ---
        # We create a stream of moving dashes to simulate trucks
        stream_down = DashedLine(UP*3.5, DOWN*3.5, dash_length=0.2, dashed_ratio=0.5, color=TERMINAL_GREEN, stroke_width=6)
        stream_up = DashedLine(DOWN*3.5, UP*3.5, dash_length=0.2, dashed_ratio=0.5, color=TERMINAL_GREEN, stroke_width=6)
        
        # --- 3. ANIMATION ---
        
        # A. Setup
        self.play(FadeIn(title), Create(highway), FadeIn(cities))
        
        # B. Normal Operations (Trucks moving)
        # We use a loop to show traffic flowing for a few seconds
        for _ in range(3):
            self.play(
                ApplyMethod(stream_down.shift, DOWN*0.5, run_time=0.5, rate_func=linear),
                ApplyMethod(stream_up.shift, UP*0.5, run_time=0.5, rate_func=linear),
            )
            # Reset position to loop smoothly
            stream_down.move_to(highway.get_center())
            stream_up.move_to(highway.get_center())

        # C. THE STRIKE (CIA Intervention)
        
        # 1. The Trigger
        trigger_text = Text("CIA FUNDS INJECTED", font="Impact", color=ALERT_RED, font_size=50)
        trigger_box = SurroundingRectangle(trigger_text, color=ALERT_RED, fill_color=BLACK, fill_opacity=0.9, buff=0.2)
        trigger = VGroup(trigger_box, trigger_text)
        
        self.play(FadeIn(trigger, scale=1.2), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(trigger), run_time=0.2)
        
        # 2. The Halt
        # Everything turns RED and STOPS
        
        # Update statuses to "CRITICAL"
        new_cities = VGroup()
        for group in cities:
            dot, label, status = group
            new_status = Text("SUPPLY: CRITICAL", font=FONT, font_size=16, color=ALERT_RED).move_to(status).align_to(status, LEFT)
            new_cities.add(VGroup(dot.copy().set_color(ALERT_RED), label.copy(), new_status))
            
        self.play(
            # Traffic lines turn red and solid (gridlock)
            highway.animate.set_color(ALERT_RED),
            FadeOut(stream_down),
            FadeOut(stream_up),
            Transform(cities, new_cities),
            run_time=0.5
        )
        
        # 3. The "No Entry" Icons
        # Flash X marks on the cities
        crosses = VGroup()
        for group in cities:
            dot = group[0]
            cross = Cross(scale_factor=0.3, color=ALERT_RED).move_to(dot)
            crosses.add(cross)
            
        self.play(ShowPassingFlash(crosses.set_stroke(width=8), time_width=0.5, run_time=1.0))
        
        # 4. Final Warning
        warning = Text("TRANSPORT SYSTEM: PARALYZED", font=FONT, font_size=36, color=ALERT_RED).to_edge(DOWN, buff=1.0)
        self.play(Write(warning))
        self.play(Wiggle(warning))
        
        self.wait(2)
        
# IMPORTANT: We change 'Scene' to 'MovingCameraScene' to fix the error
class SabotageAutopsyFonts(MovingCameraScene):
    def construct(self):
        # --- 1. THE AUTOPSY PALETTE ---
        BG_COLOR = "#080202"       # Dried Blood Black
        GRID_COLOR = "#260a0a"     # Dark Red Grid
        
        # The Organic Machine
        VISCERAL_RED = "#dc2626"   # Arterial Red
        DARK_RED = "#7f1d1d"       # Shadow Red
        ORGAN_PINK = "#fb7185"     # Inner Tissue (Glow)
        
        # The Infection
        TOXIN_YELLOW = "#facc15"   # Warning Yellow
        DIRTY_GOLD = "#b45309"     # Old Money
        
        # The Necrosis (Death)
        COLD_STEEL = "#475569"     # Surgical Instrument
        DEAD_BLACK = "#1a0505"     # Gangrene
        
        self.camera.background_color = BG_COLOR

        # --- FONT CONFIG ---
        # If you don't have these installed, Manim falls back to default.
        # But 'Arial' and 'Courier New' are safe. 
        # For the "Industrial" look, we use heavy weights.
        INDUSTRIAL_FONT = "Arial" # Ideally 'Oswald' or 'Franklin Gothic' if installed
        TERMINAL_FONT = "Courier New"
        
        # --- LAYER 1: THE LIFE SUPPORT (Background) ---
        grid = NumberPlane(
            x_range=[-20, 20, 1], y_range=[-15, 15, 1], 
            background_line_style={
                "stroke_color": GRID_COLOR, 
                "stroke_width": 2, 
                "stroke_opacity": 0.4
            },
            axis_config={"stroke_width": 0}
        )
        self.add(grid)
        
        # ECG LINE
        ecg_path = FunctionGraph(
            lambda x: 0.2 * np.sin(3 * x) + 0.1 * np.sin(10 * x),
            x_range=[-10, 10],
            color=DARK_RED,
            stroke_opacity=0.3,
            stroke_width=2
        ).move_to(DOWN*3)
        self.add(ecg_path)

        # --- LAYER 2: THE ORGAN (Chilean Core) ---
        organ_group = VGroup()
        
        # 2.1 The Valve (Custom Polygon)
        teeth_group = VGroup()
        for i in range(8):
            tooth = Polygon(
                [-0.15, 1.0, 0], [0.15, 1.0, 0], [0.25, 1.4, 0], [-0.25, 1.4, 0],
                color=VISCERAL_RED,
                fill_opacity=1,
                stroke_width=0
            ).rotate(i * 45 * DEGREES, about_point=ORIGIN)
            teeth_group.add(tooth)

        # 2.2 The Rim
        rim = Annulus(inner_radius=0.9, outer_radius=1.1, color=VISCERAL_RED, fill_opacity=0.3, stroke_width=2)
        rim_outline = Circle(radius=1.1, color=VISCERAL_RED, stroke_width=4)
        
        # 2.3 Glass Reflection
        glass_glare = Arc(radius=1.0, start_angle=PI/4, angle=PI/2, color=WHITE, stroke_width=10, stroke_opacity=0.1)
        
        # 2.4 Label (Updated Font)
        # Using a heavy sans-serif for that "Stamped" look
        label = Text("CHILE\nCORE", font=INDUSTRIAL_FONT, weight=BOLD, font_size=22, color=ORGAN_PINK).move_to(ORIGIN)
        
        organ_group.add(teeth_group, rim, rim_outline, glass_glare, label)

        # --- LAYER 3: THE ARTERIES ---
        arteries = VGroup()
        nodes = VGroup()
        
        angles = [30, 150, 270]
        for ang in angles:
            vein = DashedLine(ORIGIN, UP*2.8, dash_length=0.2, color=VISCERAL_RED, stroke_width=4).rotate(ang*DEGREES, about_point=ORIGIN)
            node = Dot(radius=0.2, color=VISCERAL_RED).move_to(vein.get_end())
            node_ring = Circle(radius=0.3, color=VISCERAL_RED, stroke_width=2).move_to(vein.get_end())
            arteries.add(vein)
            nodes.add(VGroup(node, node_ring))

        system = VGroup(organ_group, arteries, nodes)

        # --- ANIMATION START ---

        # SCENE 1: THE PULSE
        self.camera.frame.save_state()
        self.camera.frame.scale(0.6).move_to(organ_group)
        
        self.play(
            FadeIn(grid),
            SpinInFromNothing(rim),
            FadeIn(teeth_group),
            FadeIn(label),
            run_time=2
        )
        self.play(FadeIn(glass_glare), FadeIn(arteries), FadeIn(nodes))
        
        # Heartbeat
        for _ in range(2):
            self.play(system.animate.scale(1.08), run_time=0.15, rate_func=rush_into)
            self.play(system.animate.scale(1/1.08), run_time=0.4, rate_func=rush_from)
        
        self.play(
            Restore(self.camera.frame),
            Rotate(teeth_group, angle=PI, run_time=3, rate_func=linear),
            run_time=2
        )

        # SCENE 2: THE TOXIN
        self.play(self.camera.frame.animate.shift(UP * 2.2), run_time=1)
        
        # Font Change: Using a "Document/Typewriter" look for the funding
        fund_label = Text("COVERT FUNDING", font=TERMINAL_FONT, weight=BOLD, font_size=24, color=DIRTY_GOLD).to_corner(UL, buff=2).shift(DOWN*0.5 + RIGHT*0.5)
        
        gold = VGroup(*[Rectangle(width=1.0, height=0.2, color=DIRTY_GOLD, fill_opacity=0.9, stroke_width=0).shift(UP*i*0.25) for i in range(4)])
        gold.next_to(fund_label, DOWN)
        
        self.play(Write(fund_label), FadeIn(gold, shift=DOWN))
        
        # Tube & Injection
        tube_path = VMobject()
        tube_path.set_points_as_corners([
            gold.get_right() + RIGHT*0.1,
            gold.get_right() + RIGHT*1.2,
            gold.get_right() + RIGHT*1.2 + DOWN*3.2,
            organ_group.get_top() + UP*0.1
        ])
        
        tube_outline = tube_path.copy().set_color(COLD_STEEL).set_stroke(width=8, opacity=0.3)
        self.play(Create(tube_outline))
        
        bubbles = VGroup(*[Dot(radius=0.08, color=TOXIN_YELLOW) for _ in range(15)])
        
        self.play(
            gold.animate.set_color(COLD_STEEL),
            fund_label.animate.set_color(COLD_STEEL),
            LaggedStart(*[MoveAlongPath(b, tube_path, rate_func=linear) for b in bubbles], lag_ratio=0.05, run_time=2),
            organ_group.animate.set_color(TOXIN_YELLOW),
            label.animate.set_color(TOXIN_YELLOW),
        )
        
        self.play(self.camera.frame.animate.move_to(ORIGIN), run_time=1)

        # SCENE 3: THE CLAMP
        loans = VGroup(*[Arrow(start=LEFT*7, end=LEFT*2.2, color=VISCERAL_RED, stroke_width=6).shift(UP*(i*0.7 - 0.7)) for i in range(3)])
        
        jaw_top = Arc(radius=2.0, start_angle=PI/2 + PI/4, angle=PI/2, color=COLD_STEEL, stroke_width=15).shift(UP*1.5 + LEFT*1.5)
        jaw_bot = Arc(radius=2.0, start_angle=PI + PI/4, angle=PI/2, color=COLD_STEEL, stroke_width=15).shift(DOWN*1.5 + LEFT*1.5)
        
        self.play(FadeIn(loans, shift=RIGHT))
        self.play(jaw_top.animate.shift(DOWN*1.5), jaw_bot.animate.shift(UP*1.5), run_time=0.4, rate_func=rush_into)
        self.play(loans.animate.set_color(DEAD_BLACK).scale(0.8), Flash(jaw_top, color=VISCERAL_RED, flash_radius=1), run_time=0.5)
        self.play(FadeOut(loans), FadeOut(jaw_top), FadeOut(jaw_bot))

        # SCENE 4: AMPUTATION
        self.play(arteries.animate.set_color(DEAD_BLACK), nodes.animate.set_color(DEAD_BLACK), run_time=1)
        self.play(
            arteries.animate.set_opacity(0),
            nodes[0].animate.shift(UP+RIGHT).set_opacity(0),
            nodes[1].animate.shift(UP+LEFT).set_opacity(0),
            nodes[2].animate.shift(DOWN).set_opacity(0),
            run_time=2
        )

        # SCENE 5: DEATH
        self.play(
            organ_group.animate.set_color(DEAD_BLACK),
            teeth_group.animate.set_color(DEAD_BLACK),
            glass_glare.animate.set_opacity(0),
            run_time=1
        )
        
        self.play(system.animate.scale(1.1), run_time=0.1)
        self.play(system.animate.scale(0.9), run_time=0.1)
        
        self.play(self.camera.frame.animate.scale(0.5).move_to(organ_group), run_time=1.5)
        
        # Font Change: Stronger Typewriter font for the final death message
        flatline_text = Text("ECONOMY\nFLATLINED", font=TERMINAL_FONT, weight=BOLD, font_size=20, color=COLD_STEEL).move_to(ORIGIN)
        
        self.play(Transform(label, flatline_text))
        self.play(FadeOut(ecg_path), run_time=2)
        
        self.wait(2)

class TruckStrikeFinalFix(MovingCameraScene):
    def construct(self):
        # --- 1. THE PALETTE (Noir & Grit) ---
        BG_COLOR = "#0a0a0a"       # Near Pitch Black
        MAP_STROKE = "#333333"     # Dark Grey Borders
        
        # The Narrative Colors
        FLOW_WHITE = "#e5e5e5"     # Normal Supply
        BRIBE_GOLD = "#d97706"     # CIA Money
        STRIKE_RED = "#dc2626"     # Blockade
        DEAD_GREY = "#404040"      # Offline
        
        self.camera.background_color = BG_COLOR
        
        # --- LAYER 1: THE MAP ---
        # A stark, simple map of Chile's "Spine"
        map_group = VGroup()
        
        # Coastlines (Jagged Lines)
        left_coast = VMobject().set_points_as_corners([
            [-2.0, 5, 0], [-1.5, 2, 0], [-1.8, -1, 0], [-1.2, -5, 0]
        ]).set_stroke(color=MAP_STROKE, width=4)
        
        right_coast = VMobject().set_points_as_corners([
            [2.0, 5, 0], [1.5, 2, 0], [1.8, -1, 0], [1.2, -5, 0]
        ]).set_stroke(color=MAP_STROKE, width=4)
        
        # The Artery (Route 5)
        highway = Line(UP*6, DOWN*6, color=FLOW_WHITE, stroke_width=2)
        
        map_group.add(left_coast, right_coast, highway)
        self.add(map_group)

        # --- LAYER 2: THE TRUCKS ---
        # Simple, readable icons
        def make_truck():
            group = VGroup()
            cab = Square(side_length=0.25, color=FLOW_WHITE, fill_opacity=1)
            trailer = Rectangle(width=0.25, height=0.6, color=FLOW_WHITE, fill_opacity=1)
            trailer.next_to(cab, DOWN, buff=0.05)
            group.add(cab, trailer)
            return group

        trucks = VGroup()
        for i in range(6):
            t = make_truck()
            t.move_to(UP*(3.0 - i*1.2))
            trucks.add(t)
            
        self.add(trucks)

        # --- ANIMATION START ---

        # 1. THE FLOW (Normalcy)
        self.play(
            trucks.animate.shift(UP*0.5),
            run_time=1.5,
            rate_func=linear
        )

        # 2. THE INJECTION (Funding)
        # Zoom in for the hand-off
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.8), run_time=1)
        
        # Text: "CIA FUNDING"
        fund_text = Text("CIA FUNDING", font="Arial", weight=BOLD, font_size=24, color=BRIBE_GOLD)
        fund_text.to_corner(UL).shift(RIGHT*1 + DOWN*0.5)
        
        # Connection Lines (The Bribe)
        connections = VGroup()
        for t in trucks:
            # FIX: Using stroke_opacity instead of opacity to prevent crash
            l = Line(fund_text.get_bottom(), t.get_center(), color=BRIBE_GOLD, stroke_width=2, stroke_opacity=0.5)
            connections.add(l)
            
        self.play(Write(fund_text))
        self.play(
            Create(connections, lag_ratio=0.1),
            trucks.animate.set_color(BRIBE_GOLD), # Trucks bought
            run_time=1.5
        )
        self.play(FadeOut(connections))

        # 3. THE STRIKE (Blockade)
        
        # Text transforms to Alert
        strike_text = Text("STRIKE ACTIVE", font="Arial", weight=BOLD, font_size=24, color=STRIKE_RED)
        strike_text.move_to(fund_text)
        
        self.play(Transform(fund_text, strike_text))
        
        # Action: Rotate 90 degrees to block road
        self.play(
            trucks.animate.rotate(90*DEGREES).set_color(STRIKE_RED),
            highway.animate.set_color(STRIKE_RED),
            run_time=0.6,
            rate_func=rush_into
        )
        
        # Add visual "X" markers on road
        markers = VGroup()
        for t in trucks:
            m = Cross(scale_factor=0.2, color=STRIKE_RED, stroke_width=3).move_to(t)
            markers.add(m)
        self.play(FadeIn(markers))

        # 4. THE STANDSTILL (Supply Shock)
        
        # Supplies (White dots) enter
        supplies = VGroup(*[Dot(radius=0.08, color=FLOW_WHITE).move_to(DOWN*5 + UP*i*0.4) for i in range(10)])
        self.play(FadeIn(supplies))
        
        # They hit the blockade
        self.play(supplies.animate.shift(UP*2.5), run_time=1, rate_func=linear)
        
        # They turn grey (Dead)
        self.play(supplies.animate.set_color(DEAD_GREY), run_time=0.5)

        # 5. BLACKOUT (Country Dies)
        
        self.play(Restore(self.camera.frame), run_time=1.5)
        
        # Map goes dark
        self.play(
            map_group.animate.set_color(DEAD_GREY).set_opacity(0.3),
            trucks.animate.set_color(DEAD_GREY),
            markers.animate.set_color(DEAD_GREY),
            FadeOut(fund_text),
            FadeOut(supplies),
            run_time=2
        )
        
        # Final Text
        final = Text("NATIONAL STANDSTILL", font="Arial", weight=BOLD, font_size=40, color=WHITE)
        self.play(Write(final))
        
        self.wait(2)

class ChileShortageMonitor(MovingCameraScene):
    def construct(self):
        # --- 1. TACTICAL PALETTE ---
        BG_COLOR = "#050505"
        
        # Colors
        GAUGE_WHITE = "#e2e8f0"    # Full
        GAUGE_EMPTY = "#334155"    # Background of gauge
        CRISIS_RED = "#dc2626"     # Empty/Alarm
        
        self.camera.background_color = BG_COLOR
        
        # FONTS
        MAIN_FONT = "Arial" 
        TECH_FONT = "Courier New"

        # --- LAYER 1: ATMOSPHERE ---
        # Digital Grain
        noise = VGroup(*[
            Dot(
                point=[random.uniform(-8, 8), random.uniform(-5, 5), 0], 
                radius=0.02, color=GRAY, fill_opacity=random.uniform(0.05, 0.1)
            ) for _ in range(250)
        ])
        self.add(noise)

        # --- LAYER 2: SUPPLY GAUGES ---
        
        # Categories
        categories = ["FOOD", "FUEL", "PARTS"]
        gauges = VGroup()
        
        # Create 3 Vertical Bars
        for i, cat in enumerate(categories):
            # 1. The Label
            label = Text(cat, font=MAIN_FONT, weight=BOLD, font_size=36, color=GAUGE_WHITE)
            
            # 2. The Container (Border)
            border = Rectangle(width=1.5, height=4, color=GAUGE_WHITE, stroke_width=4, fill_opacity=0)
            
            # 3. The Fill (starts full)
            fill = Rectangle(width=1.3, height=3.8, color=GAUGE_WHITE, fill_opacity=0.8, stroke_width=0)
            fill.move_to(border.get_bottom() + UP*0.1, aligned_edge=DOWN)
            
            # 4. Background (Empty state)
            bg = Rectangle(width=1.3, height=3.8, color=GAUGE_EMPTY, fill_opacity=0.3, stroke_width=0)
            bg.move_to(fill)
            
            # Group them (Positioning)
            # x-offset: -3, 0, 3
            x_pos = (i - 1) * 3
            
            group = VGroup(bg, fill, border, label)
            
            # Arrange vertically: Label on bottom or top? Top looks more like a chart.
            label.next_to(border, UP, buff=0.4)
            group.move_to([x_pos, 0, 0])
            
            # Store references for animation
            group.fill_ref = fill
            group.border_ref = border
            group.label_ref = label
            
            gauges.add(group)
            
        self.play(FadeIn(gauges, lag_ratio=0.2, shift=UP*0.5), run_time=1)
        
        # --- LAYER 3: THE DRAIN ANIMATION ---
        
        # Animate the height of the 'fill' rectangles shrinking to 0
        drain_anims = []
        
        for gauge in gauges:
            # We use a ValueTracker to control the height so it looks like liquid draining
            # But simpler: Transform into a tiny sliver at the bottom
            
            target_fill = gauge.fill_ref.copy()
            target_fill.stretch_to_fit_height(0.01) # Shrink to almost nothing
            target_fill.move_to(gauge.border_ref.get_bottom() + UP*0.1, aligned_edge=DOWN)
            target_fill.set_color(CRISIS_RED) # Turn red as it empties
            
            drain_anims.append(
                Transform(gauge.fill_ref, target_fill, rate_func=linear)
            )
            
        self.play(AnimationGroup(*drain_anims, run_time=2.5))
        
        # --- LAYER 4: CRITICAL FAILURE ---
        
        # 1. Turn borders Red
        self.play(
            *[g.border_ref.animate.set_color(CRISIS_RED) for g in gauges],
            *[g.label_ref.animate.set_color(CRISIS_RED) for g in gauges],
            run_time=0.2
        )
        
        # 2. Flash Warning
        warning_text = Text("SEVERE SHORTAGE", font=MAIN_FONT, weight=BOLD, font_size=60, color=CRISIS_RED)
        warning_box = SurroundingRectangle(warning_text, color=CRISIS_RED, buff=0.3, stroke_width=8, fill_color=BG_COLOR, fill_opacity=0.8)
        warning_group = VGroup(warning_box, warning_text).rotate(5*DEGREES)
        
        self.play(
            FadeIn(warning_group, scale=2), # Slam in
            self.camera.frame.animate.set_color(CRISIS_RED), # Screen flash
            run_time=0.2,
            rate_func=rush_into
        )
        
        # 3. Restore and Shake
        self.play(
            self.camera.frame.animate.set_color(BG_COLOR),
            Wiggle(warning_group),
            run_time=0.5
        )
        
        self.wait(2)

class ChileCollapseFlatlineFinal(MovingCameraScene):
    def construct(self):
        # --- 1. TACTICAL PALETTE ---
        BG_COLOR = "#050505"
        
        # Colors
        PULSE_WHITE = "#f8fafc"    # Alive
        PULSE_RED = "#dc2626"      # Dead/Crash
        DEATH_DARK = "#450a0a"     # Dried Blood Background
        
        self.camera.background_color = BG_COLOR
        
        # FONTS
        # "Impact" is the industry standard for heavy, loud text.
        # If not found, Manim will fallback, but Impact is on almost all OS.
        IMPACT_FONT = "Impact" 
        TECH_FONT = "Courier New"

        # --- LAYER 1: ATMOSPHERE ---
        # Digital Grain
        noise = VGroup(*[
            Dot(
                point=[random.uniform(-8, 8), random.uniform(-5, 5), 0], 
                radius=0.02, color=GRAY, fill_opacity=random.uniform(0.05, 0.1)
            ) for _ in range(300)
        ])
        self.add(noise)
        
        # Single Horizon Line (The Flatline level)
        horizon = Line(LEFT*8, RIGHT*8, color=GRAY, stroke_width=2, stroke_opacity=0.3)
        horizon.move_to(DOWN*1)
        self.add(horizon)

        # --- LAYER 2: THE PULSE (THE ECONOMY) ---
        
        # Setup invisible axes for mapping points
        axes = Axes(
            x_range=[0, 10, 1], y_range=[-3, 3, 1],
            axis_config={"stroke_opacity": 0} 
        ).move_to(ORIGIN)
        
        # The EKG Line Generator
        # Phase 1: Chaos (Inflation)
        curve_points = []
        for x in range(0, 60):
            # X progresses, Y is erratic noise
            curve_points.append([x/10, random.uniform(0, 1.5) + (x/100)**2, 0]) 
            
        # Phase 2: The Crash (Sharp Drop)
        curve_points.append([6.1, 2.5, 0])  # Last gasp up
        curve_points.append([6.2, -1.0, 0]) # The drop (matches horizon y=-1 relative to center)
        
        # Phase 3: The Flatline
        for x in range(63, 100):
            curve_points.append([x/10, -1.0, 0]) # Dead line
            
        # Draw the line
        pulse_line = VMobject()
        # Scale X to fit screen better (shift left)
        pulse_line.set_points_as_corners([axes.c2p(p[0], p[1]) for p in curve_points])
        pulse_line.shift(LEFT*3.5 + DOWN*0.5)
        pulse_line.set_color(PULSE_WHITE).set_stroke(width=6)
        
        # Status Label
        status_label = Text("ECONOMIC ACTIVITY", font=TECH_FONT, weight=BOLD, font_size=24, color=PULSE_WHITE)
        status_label.to_corner(UL, buff=1)
        self.add(status_label)

        # --- ANIMATION PART 1: THE CRASH ---
        
        # Animate the drawing (Live Monitor Style)
        self.play(
            Create(pulse_line, run_time=3, rate_func=linear),
            # Camera slight pan to keep lead point in focus
            self.camera.frame.animate.shift(RIGHT*1.5),
        )
        
        # IMPACT MOMENT: When line hits bottom
        self.camera.frame.set_color(PULSE_RED) # Flash red
        self.wait(0.05)
        self.camera.frame.set_color(BG_COLOR)
        
        # Line turns red (Death)
        self.play(
            pulse_line.animate.set_color(PULSE_RED),
            status_label.animate.become(Text("SYSTEM FAILURE", font=TECH_FONT, weight=BOLD, font_size=24, color=PULSE_RED).to_corner(UL, buff=1)),
            run_time=0.1
        )

        # --- ANIMATION PART 2: THE STAMP ---
        
        # Setup the "Complete Collapse" Stamp using IMPACT font
        stamp_text = Text("COMPLETE\nCOLLAPSE", font=IMPACT_FONT, font_size=90, color=PULSE_RED, line_spacing=0.8)
        
        # Add a heavy border
        stamp_border = SurroundingRectangle(stamp_text, color=PULSE_RED, buff=0.3, stroke_width=12)
        stamp_group = VGroup(stamp_text, stamp_border).rotate(5*DEGREES).move_to(ORIGIN)
        
        # Background Chile Map (Subtle Ghost)
        try:
            chile_bg = SVGMobject("chile.svg")
            chile_bg.set_fill(DEATH_DARK, opacity=0.4)
            chile_bg.set_stroke(PULSE_RED, width=2, opacity=0.5)
            chile_bg.height = 7
            chile_bg.move_to(ORIGIN)
            self.play(FadeIn(chile_bg), run_time=0.5)
        except:
            pass # Continue if no SVG

        # SLAM ANIMATION
        self.play(
            FadeIn(stamp_group, scale=3), # Starts huge
            self.camera.frame.animate.set_color(DEATH_DARK), # Background turns bloody
            run_time=0.25,
            rate_func=rush_into # Fast slam
        )
        
        # Aftermath Shake
        self.play(
            Wiggle(stamp_group, rotation_angle=0.03*TAU),
            pulse_line.animate.set_opacity(0.3), # Fade line to background
            run_time=0.5
        )
        
        # Final slow zoom out for cinematic ending
        self.play(
            self.camera.frame.animate.scale(1.1).set_color(BG_COLOR),
            run_time=2
        )
        
        self.wait(2)

class ChileHumanCostFinal(MovingCameraScene):
    def construct(self):
        # --- 1. TACTICAL PALETTE ---
        BG_COLOR = "#050505"
        
        # Colors
        DEATH_RED = "#dc2626"      # The 3,000
        TORTURE_AMBER = "#d97706"  # The 40,000
        BOX_BG = "#000000"         # Black background for text
        
        self.camera.background_color = BG_COLOR
        
        # FONTS
        IMPACT_FONT = "Arial Black"
        DATA_FONT = "Courier New"

        # --- LAYER 1: ATMOSPHERE ---
        # Digital Grain
        noise = VGroup(*[
            Dot(
                point=[random.uniform(-15, 15), random.uniform(-10, 10), 0], 
                radius=0.03, color=GRAY, fill_opacity=random.uniform(0.05, 0.1)
            ) for _ in range(800)
        ])
        self.add(noise)

        # --- PART 1: THE 3,000 DEAD (Intimate View) ---
        
        # Dense block representing the dead
        dead_group = VGroup()
        for i in range(12): 
            for j in range(25):
                line = Rectangle(height=0.4, width=0.08, fill_color=DEATH_RED, fill_opacity=0.9, stroke_width=0)
                line.move_to([i*0.15 - 0.9, j*0.4 - 5, 0])
                dead_group.add(line)
        
        dead_group.move_to(ORIGIN)
        
        # Text 1: 3,000 DEAD
        death_count_text = Text("3,000+", font=IMPACT_FONT, font_size=80, color=DEATH_RED)
        death_label = Text("EXECUTED / DISAPPEARED", font=DATA_FONT, weight=BOLD, font_size=24, color=DEATH_RED)
        death_raw_text = VGroup(death_count_text, death_label).arrange(DOWN, buff=0.2)
        
        # BOX 1: The background for the 3,000 text
        death_bg_box = SurroundingRectangle(
            death_raw_text, 
            color=BOX_BG, 
            fill_color=BOX_BG, 
            fill_opacity=0.85, 
            buff=0.3, 
            stroke_width=0
        )
        
        death_final_group = VGroup(death_bg_box, death_raw_text).move_to(ORIGIN).scale(0.5)

        # ANIMATION 1: Zoomed In
        self.camera.frame.save_state()
        self.camera.frame.set_height(dead_group.height * 1.5).move_to(dead_group)
        
        self.play(
            FadeIn(dead_group, lag_ratio=0.01, run_time=1.5),
            FadeIn(death_final_group, scale=1.5),
        )
        self.wait(0.5)
        
        # --- PART 2: THE REVEAL (40,000 TORTURED) ---
        
        # Move death text out of the way (keeping the box)
        self.play(
            death_final_group.animate.scale(1.5).next_to(dead_group, UP, buff=0.5),
            run_time=0.5
        )

        # Create the massive field of Torture Victims
        torture_group = VGroup()
        for _ in range(2000): 
            x = random.uniform(-12, 12)
            y = random.uniform(-7, 7)
            if abs(x) < 2 and abs(y) < 3: continue 
            dot = Square(side_length=0.09, fill_color=TORTURE_AMBER, fill_opacity=0.5, stroke_width=0)
            dot.move_to([x, y, 0])
            torture_group.add(dot)
            
        # Text 2: 40,000 TORTURED
        torture_count_text = Text("40,000+", font=IMPACT_FONT, font_size=120, color=TORTURE_AMBER)
        torture_label = Text("TORTURE VICTIMS", font=DATA_FONT, weight=BOLD, font_size=50, color=TORTURE_AMBER)
        torture_raw_text = VGroup(torture_count_text, torture_label).arrange(DOWN, buff=0.2)
        
        # BOX 2: The background for the 40,000 text
        torture_bg_box = SurroundingRectangle(
            torture_raw_text, 
            color=BOX_BG,          
            fill_color=BOX_BG,     
            fill_opacity=0.85,     
            buff=0.4, 
            stroke_width=0         
        )
        
        torture_final_group = VGroup(torture_bg_box, torture_raw_text).move_to(ORIGIN)

        # ANIMATION 2: The Violent Zoom Out
        self.play(
            # 1. Camera pulls back
            Restore(self.camera.frame, run_time=3, rate_func=exponential_decay),
            
            # 2. Orange dots appear
            FadeIn(torture_group, lag_ratio=0.02, run_time=2.5),
            
            # 3. Old text fades out, New text fades in
            FadeOut(death_final_group, run_time=0.5),
            FadeIn(torture_final_group, scale=0.8, run_time=1.5)
        )
        
        # Final Impact - Blood Red Shift
        self.play(
            Flash(torture_final_group, color=DEATH_RED, flash_radius=5, num_lines=40),
            torture_group.animate.set_color(DEATH_RED).set_opacity(0.3),
            torture_count_text.animate.set_color(DEATH_RED),
            torture_label.animate.set_color(DEATH_RED),
            run_time=0.5
        )
        
        self.wait(2)


class ChilePuppetLogoReady(MovingCameraScene):
    def construct(self):
        # --- 1. NOIR PALETTE ---
        BG_COLOR = "#0a0a0a"
        STRING_RED = "#ef4444"     # The Control Lines
        MAP_WHITE = "#e5e5e5"      # Innocent State
        MAP_RED = "#7f1d1d"        # Captured State
        
        self.camera.background_color = BG_COLOR

        # --- LAYER 1: ATMOSPHERE ---
        # Subtle spotlight to give depth
        spotlight = Circle(radius=8, color=WHITE, fill_opacity=0.02).set_stroke(width=0)
        self.add(spotlight)
        
        # --- PART 1: THE TARGET (Chile) ---
        
        # Draw the placeholder map
        target_map = RoundedRectangle(corner_radius=0.2, height=5, width=1.5, color=MAP_WHITE, fill_opacity=0.8).set_stroke(width=0)
        target_map.move_to(DOWN * 2)
        
        # Label
        map_label = Text("CHILE", font="Courier New", weight=BOLD, font_size=24, color=BLACK).move_to(target_map)
        
        map_group = VGroup(target_map, map_label)
        self.play(FadeIn(map_group, shift=UP*0.5), run_time=1.5)
        
        # --- PART 2: THE STRINGS DESCEND ---
        
        # LOWERED START POINT (As requested)
        # Previously UP*9, now UP*5 to keep them accessible
        string_start_y = UP*5 
        
        start_points = [
            string_start_y + LEFT*1.5, 
            string_start_y + LEFT*0.5, 
            string_start_y + RIGHT*0.5, 
            string_start_y + RIGHT*1.5
        ]
        
        # End points on the map
        end_points = [
            target_map.get_top() + LEFT*0.4, 
            target_map.get_top() + LEFT*0.1, 
            target_map.get_top() + RIGHT*0.1, 
            target_map.get_top() + RIGHT*0.4
        ]
        
        strings = VGroup()
        for sp, ep in zip(start_points, end_points):
            l = Line(sp, sp, color=STRING_RED, stroke_width=4)
            l.target_end = ep
            strings.add(l)
            
        self.add(strings)
        
        # Animation: Strings shoot down violently
        anims = []
        for l in strings:
            anims.append(l.animate.put_start_and_end_on(l.get_start(), l.target_end))
            
        self.play(AnimationGroup(*anims, lag_ratio=0.05, run_time=0.7, rate_func=rush_into))
        
        # --- PART 3: THE CAPTURE ---
        
        # Flashes
        flash_anims = [Flash(l.target_end, color=STRING_RED, flash_radius=0.5, run_time=0.3) for l in strings]
        
        self.play(
            *flash_anims, 
            target_map.animate.set_color(MAP_RED),
            map_label.animate.set_color(STRING_RED),
            run_time=0.2
        )
        
        # --- PART 4: THE JERK & REVEAL ---
        
        # 1. Pull the map UP
        lift_amount = UP * 2.5
        
        # We animate the lines moving UP (both start and end points)
        # This simulates the puppeteer pulling them upward
        string_anims = [l.animate.put_start_and_end_on(l.get_start()+lift_amount, l.get_end()+lift_amount) for l in strings]
        
        self.play(
            map_group.animate.shift(lift_amount).rotate(4*DEGREES), 
            *string_anims,
            run_time=1.8,
            rate_func=smooth 
        )
        
        # 2. Camera Pans UP to the "Logo Space"
        # We pan to center on UP*6.
        # Since strings start at UP*5 + UP*2.5 (lift) = UP*7.5
        # And camera top edge will be around UP*10.
        # This leaves plenty of space at the top.
        self.play(
            self.camera.frame.animate.move_to(UP*6),
            run_time=2.5,
            rate_func=smooth
        )
        
        # 3. Hold for Logo placement
        self.wait(3)
import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

def solve_law_of_cosines(a, b, c, A, B, C):
    """
    Solve triangle using Law of Cosines
    Sides: a, b, c (opposite to angles A, B, C respectively)
    Angles: A, B, C in degrees
    """
    results = []
    steps = []
    
    # Convert angles to radians for calculation
    A_rad = math.radians(A) if A else None
    B_rad = math.radians(B) if B else None
    C_rad = math.radians(C) if C else None
    
    try:
        # Count known values
        known_sides = sum([1 for x in [a, b, c] if x is not None and x > 0])
        known_angles = sum([1 for x in [A, B, C] if x is not None and x > 0])
        
        # Case 1: Three sides known (SSS) - find all angles
        if known_sides == 3 and known_angles == 0:
            steps.append("### 📚 Step-by-Step Solution (SSS Case)")
            steps.append(f"\n**Given:** a = {a}, b = {b}, c = {c}")
            steps.append("\n---")
            
            # Find angle A: cos(A) = (b² + c² - a²) / (2bc)
            steps.append(f"\n**Step 1: Find Angle A using Law of Cosines**")
            steps.append(f"Formula: cos(A) = (b² + c² - a²) / (2bc)")
            steps.append(f"\nSubstitute values:")
            steps.append(f"cos(A) = ({b}² + {c}² - {a}²) / (2 × {b} × {c})")
            steps.append(f"cos(A) = ({b**2} + {c**2} - {a**2}) / ({2*b*c})")
            cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
            steps.append(f"cos(A) = {cos_A:.6f}")
            A_rad = math.acos(np.clip(cos_A, -1, 1))
            A = math.degrees(A_rad)
            steps.append(f"A = arccos({cos_A:.6f}) = **{A:.4f}°**")
            
            # Find angle B: cos(B) = (a² + c² - b²) / (2ac)
            steps.append(f"\n**Step 2: Find Angle B using Law of Cosines**")
            steps.append(f"Formula: cos(B) = (a² + c² - b²) / (2ac)")
            steps.append(f"\nSubstitute values:")
            steps.append(f"cos(B) = ({a}² + {c}² - {b}²) / (2 × {a} × {c})")
            steps.append(f"cos(B) = ({a**2} + {c**2} - {b**2}) / ({2*a*c})")
            cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
            steps.append(f"cos(B) = {cos_B:.6f}")
            B_rad = math.acos(np.clip(cos_B, -1, 1))
            B = math.degrees(B_rad)
            steps.append(f"B = arccos({cos_B:.6f}) = **{B:.4f}°**")
            
            # Find angle C: C = 180 - A - B
            steps.append(f"\n**Step 3: Find Angle C using angle sum property**")
            steps.append(f"Formula: A + B + C = 180°")
            steps.append(f"\nC = 180° - A - B")
            steps.append(f"C = 180° - {A:.4f}° - {B:.4f}°")
            C = 180 - A - B
            C_rad = math.radians(C)
            steps.append(f"C = **{C:.4f}°**")
            
            results.append(f"**Solution (SSS Case):**")
            results.append(f"- Side a = {a:.4f}")
            results.append(f"- Side b = {b:.4f}")
            results.append(f"- Side c = {c:.4f}")
            results.append(f"- Angle A = {A:.4f}°")
            results.append(f"- Angle B = {B:.4f}°")
            results.append(f"- Angle C = {C:.4f}°")
        
        # Case 2: Two sides and included angle (SAS) - find third side and other angles
        elif known_sides == 2 and known_angles == 1:
            steps.append("### 📚 Step-by-Step Solution (SAS Case)")
            
            if a and b and C_rad:
                steps.append(f"\n**Given:** a = {a}, b = {b}, C = {C}°")
                steps.append("\n---")
                
                # Find side c: c² = a² + b² - 2ab·cos(C)
                steps.append(f"\n**Step 1: Find Side c using Law of Cosines**")
                steps.append(f"Formula: c² = a² + b² - 2ab·cos(C)")
                steps.append(f"\nSubstitute values:")
                steps.append(f"c² = {a}² + {b}² - 2({a})({b})·cos({C}°)")
                steps.append(f"c² = {a**2} + {b**2} - {2*a*b}·cos({C}°)")
                c_squared = a**2 + b**2 - 2*a*b*math.cos(C_rad)
                steps.append(f"c² = {a**2} + {b**2} - {2*a*b*math.cos(C_rad):.6f}")
                steps.append(f"c² = {c_squared:.6f}")
                c = math.sqrt(c_squared)
                steps.append(f"c = √{c_squared:.6f} = **{c:.4f}**")
                
                # Find angle A
                steps.append(f"\n**Step 2: Find Angle A using Law of Cosines**")
                steps.append(f"Formula: cos(A) = (b² + c² - a²) / (2bc)")
                steps.append(f"\nSubstitute values:")
                steps.append(f"cos(A) = ({b}² + {c:.4f}² - {a}²) / (2 × {b} × {c:.4f})")
                cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
                steps.append(f"cos(A) = {cos_A:.6f}")
                A_rad = math.acos(np.clip(cos_A, -1, 1))
                A = math.degrees(A_rad)
                steps.append(f"A = arccos({cos_A:.6f}) = **{A:.4f}°**")
                
                # Find angle B
                steps.append(f"\n**Step 3: Find Angle B using angle sum property**")
                steps.append(f"B = 180° - A - C")
                steps.append(f"B = 180° - {A:.4f}° - {C}°")
                B = 180 - A - C
                B_rad = math.radians(B)
                steps.append(f"B = **{B:.4f}°**")
                
            elif a and c and B_rad:
                steps.append(f"\n**Given:** a = {a}, c = {c}, B = {B}°")
                steps.append("\n---")
                
                # Find side b: b² = a² + c² - 2ac·cos(B)
                steps.append(f"\n**Step 1: Find Side b using Law of Cosines**")
                steps.append(f"Formula: b² = a² + c² - 2ac·cos(B)")
                steps.append(f"\nSubstitute values:")
                steps.append(f"b² = {a}² + {c}² - 2({a})({c})·cos({B}°)")
                b_squared = a**2 + c**2 - 2*a*c*math.cos(B_rad)
                steps.append(f"b² = {b_squared:.6f}")
                b = math.sqrt(b_squared)
                steps.append(f"b = √{b_squared:.6f} = **{b:.4f}**")
                
                # Find angle A
                steps.append(f"\n**Step 2: Find Angle A using Law of Cosines**")
                steps.append(f"Formula: cos(A) = (b² + c² - a²) / (2bc)")
                cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
                steps.append(f"cos(A) = {cos_A:.6f}")
                A_rad = math.acos(np.clip(cos_A, -1, 1))
                A = math.degrees(A_rad)
                steps.append(f"A = **{A:.4f}°**")
                
                # Find angle C
                steps.append(f"\n**Step 3: Find Angle C**")
                steps.append(f"C = 180° - A - B")
                C = 180 - A - B
                C_rad = math.radians(C)
                steps.append(f"C = **{C:.4f}°**")
                
            elif b and c and A_rad:
                steps.append(f"\n**Given:** b = {b}, c = {c}, A = {A}°")
                steps.append("\n---")
                
                # Find side a: a² = b² + c² - 2bc·cos(A)
                steps.append(f"\n**Step 1: Find Side a using Law of Cosines**")
                steps.append(f"Formula: a² = b² + c² - 2bc·cos(A)")
                steps.append(f"\nSubstitute values:")
                steps.append(f"a² = {b}² + {c}² - 2({b})({c})·cos({A}°)")
                a_squared = b**2 + c**2 - 2*b*c*math.cos(A_rad)
                steps.append(f"a² = {a_squared:.6f}")
                a = math.sqrt(a_squared)
                steps.append(f"a = √{a_squared:.6f} = **{a:.4f}**")
                
                # Find angle B
                steps.append(f"\n**Step 2: Find Angle B using Law of Cosines**")
                steps.append(f"Formula: cos(B) = (a² + c² - b²) / (2ac)")
                cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
                steps.append(f"cos(B) = {cos_B:.6f}")
                B_rad = math.acos(np.clip(cos_B, -1, 1))
                B = math.degrees(B_rad)
                steps.append(f"B = **{B:.4f}°**")
                
                # Find angle C
                steps.append(f"\n**Step 3: Find Angle C**")
                steps.append(f"C = 180° - A - B")
                C = 180 - A - B
                C_rad = math.radians(C)
                steps.append(f"C = **{C:.4f}°**")
            
            results.append(f"**Solution (SAS Case):**")
            results.append(f"- Side a = {a:.4f}")
            results.append(f"- Side b = {b:.4f}")
            results.append(f"- Side c = {c:.4f}")
            results.append(f"- Angle A = {A:.4f}°")
            results.append(f"- Angle B = {B:.4f}°")
            results.append(f"- Angle C = {C:.4f}°")
        
        # Case 3: One side and two angles - find other sides
        elif known_sides == 1 and known_angles == 2:
            steps.append("### 📚 Step-by-Step Solution (ASA/AAS Case)")
            
            # First find the third angle
            if A and B:
                steps.append(f"\n**Given:** A = {A}°, B = {B}°, and one side")
                steps.append("\n---")
                steps.append(f"\n**Step 1: Find Angle C**")
                steps.append(f"A + B + C = 180°")
                steps.append(f"C = 180° - A - B")
                steps.append(f"C = 180° - {A}° - {B}°")
                C = 180 - A - B
                C_rad = math.radians(C)
                steps.append(f"C = **{C:.4f}°**")
            elif A and C:
                steps.append(f"\n**Given:** A = {A}°, C = {C}°, and one side")
                steps.append("\n---")
                steps.append(f"\n**Step 1: Find Angle B**")
                steps.append(f"B = 180° - A - C")
                B = 180 - A - C
                B_rad = math.radians(B)
                steps.append(f"B = **{B:.4f}°**")
            elif B and C:
                steps.append(f"\n**Given:** B = {B}°, C = {C}°, and one side")
                steps.append("\n---")
                steps.append(f"\n**Step 1: Find Angle A**")
                steps.append(f"A = 180° - B - C")
                A = 180 - B - C
                A_rad = math.radians(A)
                steps.append(f"A = **{A:.4f}°**")
            
            # Use Law of Sines to find other sides
            if a:
                steps.append(f"\n**Step 2: Find Side b using Law of Sines**")
                steps.append(f"Formula: a/sin(A) = b/sin(B)")
                steps.append(f"b = a × sin(B) / sin(A)")
                steps.append(f"b = {a} × sin({B:.4f}°) / sin({A:.4f}°)")
                b = a * math.sin(B_rad) / math.sin(A_rad)
                steps.append(f"b = **{b:.4f}**")
                
                steps.append(f"\n**Step 3: Find Side c using Law of Sines**")
                steps.append(f"c = a × sin(C) / sin(A)")
                steps.append(f"c = {a} × sin({C:.4f}°) / sin({A:.4f}°)")
                c = a * math.sin(C_rad) / math.sin(A_rad)
                steps.append(f"c = **{c:.4f}**")
                
            elif b:
                steps.append(f"\n**Step 2: Find Side a using Law of Sines**")
                steps.append(f"a = b × sin(A) / sin(B)")
                a = b * math.sin(A_rad) / math.sin(B_rad)
                steps.append(f"a = **{a:.4f}**")
                
                steps.append(f"\n**Step 3: Find Side c using Law of Sines**")
                steps.append(f"c = b × sin(C) / sin(B)")
                c = b * math.sin(C_rad) / math.sin(B_rad)
                steps.append(f"c = **{c:.4f}**")
                
            elif c:
                steps.append(f"\n**Step 2: Find Side a using Law of Sines**")
                steps.append(f"a = c × sin(A) / sin(C)")
                a = c * math.sin(A_rad) / math.sin(C_rad)
                steps.append(f"a = **{a:.4f}**")
                
                steps.append(f"\n**Step 3: Find Side b using Law of Sines**")
                steps.append(f"b = c × sin(B) / sin(C)")
                b = c * math.sin(B_rad) / math.sin(C_rad)
                steps.append(f"b = **{b:.4f}**")
            
            results.append(f"**Solution (ASA/AAS Case):**")
            results.append(f"- Side a = {a:.4f}")
            results.append(f"- Side b = {b:.4f}")
            results.append(f"- Side c = {c:.4f}")
            results.append(f"- Angle A = {A:.4f}°")
            results.append(f"- Angle B = {B:.4f}°")
            results.append(f"- Angle C = {C:.4f}°")
        
        else:
            return "❌ Insufficient or invalid information. Please provide:\n- Three sides (SSS)\n- Two sides and included angle (SAS)\n- One side and two angles (ASA/AAS)", "", None
        
        # Validate triangle inequality
        if not (a + b > c and a + c > b and b + c > a):
            return "❌ Invalid triangle: sides do not satisfy triangle inequality", "", None
        
        # Create visualization
        fig = plot_triangle(a, b, c, A, B, C)
        
        return "\n".join(results), "\n".join(steps), fig
        
    except Exception as e:
        return f"❌ Error: {str(e)}\nPlease check your inputs.", "", None

def plot_triangle(a, b, c, A, B, C):
    """Plot the triangle to scale"""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Place vertex C at origin, vertex B on x-axis
    C_point = np.array([0, 0])
    B_point = np.array([a, 0])
    
    # Calculate position of vertex A using angle C
    C_rad = math.radians(C)
    A_point = np.array([b * math.cos(C_rad), b * math.sin(C_rad)])
    
    # Create triangle
    triangle = np.array([A_point, B_point, C_point])
    
    # Plot triangle
    poly = Polygon(triangle, fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(poly)
    
    # Plot vertices
    ax.plot(*A_point, 'ro', markersize=10, label='Vertex A')
    ax.plot(*B_point, 'go', markersize=10, label='Vertex B')
    ax.plot(*C_point, 'bo', markersize=10, label='Vertex C')
    
    # Label vertices
    offset = max(a, b, c) * 0.05
    ax.text(A_point[0], A_point[1] + offset, f'A\n({A:.1f}°)', 
            ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.text(B_point[0], B_point[1] + offset, f'B\n({B:.1f}°)', 
            ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.text(C_point[0], C_point[1] - offset, f'C\n({C:.1f}°)', 
            ha='center', va='top', fontsize=12, fontweight='bold')
    
    # Label sides
    mid_ab = (A_point + B_point) / 2
    mid_bc = (B_point + C_point) / 2
    mid_ca = (C_point + A_point) / 2
    
    ax.text(mid_ab[0], mid_ab[1] + offset, f'c = {c:.2f}', 
            ha='center', va='bottom', fontsize=10, color='red')
    ax.text(mid_bc[0], mid_bc[1] - offset, f'a = {a:.2f}', 
            ha='center', va='top', fontsize=10, color='red')
    ax.text(mid_ca[0] - offset, mid_ca[1], f'b = {b:.2f}', 
            ha='right', va='center', fontsize=10, color='red')
    
    # Set equal aspect ratio and margins
    ax.set_aspect('equal')
    margin = max(a, b, c) * 0.2
    ax.set_xlim(-margin, max(a, A_point[0]) + margin)
    ax.set_ylim(-margin, A_point[1] + margin)
    
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_title('Triangle Visualization (To Scale)', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

def process_inputs(a_input, b_input, c_input, A_input, B_input, C_input):
    """Process inputs and convert empty strings to None"""
    a = float(a_input) if a_input else None
    b = float(b_input) if b_input else None
    c = float(c_input) if c_input else None
    A = float(A_input) if A_input else None
    B = float(B_input) if B_input else None
    C = float(C_input) if C_input else None
    
    return solve_law_of_cosines(a, b, c, A, B, C)

# Create Gradio interface
with gr.Blocks(title="Law of Cosines Solver") as app:
    gr.Markdown("""
    # 📐 Law of Cosines Triangle Solver
    
    **Instructions:**
    - Enter known values for sides (a, b, c) and/or angles (A, B, C)
    - Leave unknown values blank
    - Supported cases:
        - **SSS**: Three sides → finds all angles
        - **SAS**: Two sides and included angle → finds third side and other angles
        - **ASA/AAS**: One side and two angles → finds other sides
    
    **Note:** Side *a* is opposite to angle *A*, side *b* is opposite to angle *B*, and side *c* is opposite to angle *C*
    """)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📏 Sides")
            a_input = gr.Number(label="Side a", placeholder="Enter value or leave blank")
            b_input = gr.Number(label="Side b", placeholder="Enter value or leave blank")
            c_input = gr.Number(label="Side c", placeholder="Enter value or leave blank")
        
        with gr.Column():
            gr.Markdown("### 📐 Angles (in degrees)")
            A_input = gr.Number(label="Angle A (degrees)", placeholder="Enter value or leave blank")
            B_input = gr.Number(label="Angle B (degrees)", placeholder="Enter value or leave blank")
            C_input = gr.Number(label="Angle C (degrees)", placeholder="Enter value or leave blank")
    
    solve_btn = gr.Button("🔍 Solve Triangle", variant="primary", size="lg")
    
    with gr.Row():
        with gr.Column(scale=1):
            result_output = gr.Markdown(label="Results")
        with gr.Column(scale=2):
            plot_output = gr.Plot(label="Triangle Visualization")
    
    gr.Markdown("---")
    steps_output = gr.Markdown(label="Step-by-Step Solution")
    
    # Examples
    gr.Markdown("### 📝 Example Cases")
    gr.Examples(
        examples=[
            [3, 4, 5, None, None, None],  # SSS - Right triangle
            [5, 7, None, None, None, 60],  # SAS
            [None, None, 10, 30, 60, None],  # ASA
            [8, 10, 12, None, None, None],  # SSS - Scalene
        ],
        inputs=[a_input, b_input, c_input, A_input, B_input, C_input],
        label="Click to load example"
    )
    
    solve_btn.click(
        fn=process_inputs,
        inputs=[a_input, b_input, c_input, A_input, B_input, C_input],
        outputs=[result_output, steps_output, plot_output]
    )

# Launch the app
if __name__ == "__main__":
    app.launch()
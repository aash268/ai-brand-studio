"""
AI Brand Studio - Flask Backend
--------------------------------
Generates Logos, Posters, and Banners using SD-Turbo.
AI creates layout, Python overlays correct text.
"""

from flask import Flask, render_template, request, jsonify
from generate_image import SDTurboGenerator
from PIL import ImageDraw, ImageFont
from io import BytesIO
import base64

app = Flask(__name__)

print("Loading SD-Turbo model...")
generator = SDTurboGenerator()
print("Model ready!\n")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json

    design_type = data.get("type", "logo")
    name = data.get("name", "").strip()
    industry = data.get("industry", "").strip()
    style = data.get("style", "").strip()
    theme = data.get("theme", "").strip()

    if not name:
        return jsonify({"error": True, "message": "Name is required"}), 400

    # ---------- AI PROMPTS (NO TEXT INSIDE) ----------
    if design_type == "logo":
        prompt = f"""
        Professional vector logo icon for a {industry} business,
        {style} style, {theme} theme,
        minimalist symbol, clean branding,
        white background, no text, no letters
        """
        width, height = 512, 512

    elif design_type == "poster":
        prompt = f"""
        Professional event poster background for {industry},
        {style} style, {theme} theme,
        modern layout, space for headline text,
        high resolution
        """
        width, height = 512, 768

    else:  # banner
        prompt = f"""
        Professional website banner background for {industry},
        {style} style, {theme} theme,
        clean layout with empty space for text,
        modern high resolution design
        """
        width, height = 768, 384

    try:
        # ---------- Generate Background ----------
        image = generator.generate(
            prompt=prompt,
            num_inference_steps=3,
            width=width,
            height=height
        )

        # ---------- Overlay Text ----------
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype("arial.ttf", int(height * 0.08))
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        if design_type == "logo":
            x = (width - text_width) // 2
            y = height - text_height - 30

        elif design_type == "poster":
            x = (width - text_width) // 2
            y = height // 3

        else:  # banner
            x = 40
            y = (height - text_height) // 2

        draw.text((x, y), name, fill="black", font=font)

        # ---------- Convert to Base64 ----------
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            "success": True,
            "image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        return jsonify({
            "error": True,
            "message": str(e)
        }), 500


if __name__ == '__main__':
    print("=" * 50)
    print("AI BRAND STUDIO RUNNING")
    print("http://localhost:5000")
    print("=" * 50)

    app.run(debug=True, host='0.0.0.0', port=5000)
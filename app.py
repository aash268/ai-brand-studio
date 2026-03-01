from flask import Flask, render_template, request, jsonify
from diffusers import AutoPipelineForText2Image
import torch
from PIL import ImageDraw, ImageFont
import os

app = Flask(__name__)

# -----------------------------
# DEVICE SETUP
# -----------------------------
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# -----------------------------
# LOAD SD-TURBO (NO SCHEDULER EDITS)
# -----------------------------
pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=dtype,
    safety_checker=None
).to(device)

pipe.set_progress_bar_config(disable=True)

print(f"Model loaded successfully on {device.upper()}")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    main_text = data.get("main_text", "")
    sub_text = data.get("sub_text", "")
    color_style = data.get("color_style", "modern")
    tagline = data.get("tagline", "")

    # Simple stable prompt
    prompt = f"{color_style} professional graphic design, clean layout, high quality"

    # 🔥 DO NOT override steps or scheduler
    image = pipe(
        prompt=prompt,
        guidance_scale=0.0
    ).images[0]

    # -----------------------------
    # TEXT OVERLAY
    # -----------------------------
    draw = ImageDraw.Draw(image)

    try:
        main_font = ImageFont.truetype("arial.ttf", 60)
        sub_font = ImageFont.truetype("arial.ttf", 40)
    except:
        main_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    width, height = image.size

    # Center main text
    bbox = draw.textbbox((0, 0), main_text, font=main_font)
    text_width = bbox[2] - bbox[0]
    x = (width - text_width) / 2
    y = height * 0.7

    draw.text(
        (x, y),
        main_text,
        fill="white",
        font=main_font,
        stroke_width=2,
        stroke_fill="black"
    )

    if sub_text:
        draw.text(
            (x, y + 70),
            sub_text,
            fill="white",
            font=sub_font,
            stroke_width=2,
            stroke_fill="black"
        )

    if tagline:
        draw.text(
            (x, y + 120),
            tagline,
            fill="white",
            font=sub_font,
            stroke_width=2,
            stroke_fill="black"
        )

    # -----------------------------
    # SAVE IMAGE
    # -----------------------------
    os.makedirs("static/generated", exist_ok=True)
    file_path = "static/generated/output.png"
    image.save(file_path)

    return jsonify({"image_url": "/" + file_path})


if __name__ == "__main__":
    app.run(debug=True)
"""
SD-Turbo: Fast Local Image Generation
--------------------------------------
Stable Diffusion Turbo for ultra-fast local GPU image generation.
Model: stabilityai/sd-turbo
"""

import torch
from diffusers import AutoPipelineForText2Image
from PIL import Image
import time


class SDTurboGenerator:
    """
    Fast image generator using SD-Turbo model with GPU acceleration.
    """

    def __init__(self, model_id: str = "stabilityai/sd-turbo"):
        """
        Initialize SD-Turbo pipeline with auto device detection.
        """

        # ✅ AUTO detect device safely
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_id = model_id

        print(f"Loading {model_id}...")
        print(f"Using device: {self.device}")

        # Load model with correct precision
        if self.device == "cuda":
            self.pipe = AutoPipelineForText2Image.from_pretrained(
                model_id,
                torch_dtype=torch.float16,
                variant="fp16",
            )
        else:
            self.pipe = AutoPipelineForText2Image.from_pretrained(
                model_id,
                torch_dtype=torch.float32,
            )

        self.pipe = self.pipe.to(self.device)

        # Enable xFormers (optional but faster)
        if self.device == "cuda":
            try:
                self.pipe.enable_xformers_memory_efficient_attention()
                print("xFormers enabled")
            except Exception as e:
                print(f"xFormers not available: {e}")

        # Disable safety checker (faster)
        self.pipe.safety_checker = None

        print("Model loaded successfully!\n")

    def generate(
        self,
        prompt: str,
        num_inference_steps: int = 3,
        guidance_scale: float = 0.0,
        width: int = 512,
        height: int = 512,
        seed: int = None
    ) -> Image.Image:
        """
        Generate image from text prompt.
        """

        generator = None
        if seed is not None:
            generator = torch.Generator(device=self.device).manual_seed(seed)

        start_time = time.time()

        image = self.pipe(
            prompt=prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height,
            generator=generator,
        ).images[0]

        elapsed = time.time() - start_time
        print(f"Generated in {elapsed:.2f}s")

        return image
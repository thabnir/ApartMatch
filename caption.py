import requests
from PIL import Image
from transformers import GPT2TokenizerFast, ViTImageProcessor, VisionEncoderDecoderModel

image_processor = ViTImageProcessor.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)
tokenizer = GPT2TokenizerFast.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
# model_trained = joblib.load("image_captioning_model.joblib")
model_raw = VisionEncoderDecoderModel.from_pretrained(
    "nlpconnect/vit-gpt2-image-captioning"
)


def caption_image(url: str, greedy=True, debug=False) -> str:
    image = Image.open(requests.get(url, stream=True).raw)
    pixel_values = image_processor(image, return_tensors="pt").pixel_values

    if greedy:
        generated_ids = model_raw.generate(pixel_values, max_new_tokens=10000)
    else:
        generated_ids = model_raw.generate(
            pixel_values, do_sample=True, max_new_tokens=10000, top_k=5
        )
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    if debug:
        print(f'Captioning image at url: "{url}"')
        print(generated_text)
    return generated_text

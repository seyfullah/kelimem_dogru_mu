from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

def run(url):
    image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
    pixel_values = processor(images=image, return_tensors="pt").pixel_values

    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print("url", url)
    print("generated_text")
    print(generated_text)

run('https://as1.ftcdn.net/v2/jpg/03/19/85/08/1000_F_319850881_yXizkXxTpU0SixwgeCoZRUZhOKLNJV78.jpg')
run('https://www.merhabahaber.com/d/assets/facebook-default-share.png')
run('https://thumbs.dreamstime.com/z/merhaba-formal-turkish-word-hello-handwritten-white-background-171060004.jpg')
run('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGZWG8q4SJhsLAZgM3612SnWYIBzU6T96pfA&usqp=CAU')
run('https://seeklogo.com/images/M/Merhaba-logo-29B0015EF4-seeklogo.com.gif')
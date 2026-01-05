import gradio as gr
from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch

# Fast image processor (torchvision irukku, so safe)
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-vqa-base",
    use_fast=True
)

model = BlipForQuestionAnswering.from_pretrained(
    "Salesforce/blip-vqa-base"
)

def answer_question(image, question):
    try:
        inputs = processor(
            image,
            question,
            return_tensors="pt"
        )

        outputs = model.generate(**inputs)
        answer = processor.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return answer

    except Exception as e:
        return "Error occurred. Try another image or question."

iface = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Ask a question about the image")
    ],
    outputs=gr.Textbox(label="Answer"),
    title="🤖 Visual Question Answering (BLIP + Fast Processor)",
    description="Multimodal AI using BLIP with torchvision acceleration"
)

iface.launch()

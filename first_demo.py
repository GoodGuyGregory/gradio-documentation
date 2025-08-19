import gradio as gr

def greet(name, intensity: int):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text",gr.Slider(value=2, minimum=1, maximum=5, step=1)],
    outputs=[gr.Textbox(label="Greeting", lines=3)]
)

demo.launch()
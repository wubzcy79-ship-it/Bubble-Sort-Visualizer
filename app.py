import gradio as gr

# detach the list which user's input in an array and store it in a list
def parse_input_list(text: str):
    if not text:
        raise ValueError("Please enter a list of integers.")

    text = text.replace(",", " ")
    parts = text.split()

    nums = []
    for p in parts:
        try:# check if they are valid or invalid
            nums.append(int(p))
        except ValueError:
            raise ValueError(f"'{p}' is not a valid integer.")
    if len(nums) == 0:
        raise ValueError("No valid integers found.")
    return nums


# do bubble sort and record each step
def bubble_sort_with_steps(arr):
    a = arr[:]
    n = len(a)
    steps = []
    step_id = 1

    steps.append(f"Initial array: {a}")

    for i in range(n - 1):
        swapped = False
        steps.append(f"\n--- Pass {i + 1} ---")

        for j in range(n - i - 1):
            # mark the first and the second elements which compared befoe
            marked = []
            for k, val in enumerate(a):
                if k == j or k == j + 1:
                    marked.append(f"({val})")
                else:
                    marked.append(str(val))
            state = "[" + ", ".join(marked) + "]"

            info = f"Step {step_id}: {state} -> compare {a[j]} and {a[j+1]}"

            # the most importat step for bubble sort：swap them if left > right
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                info += " -> swap"
            else:
                info += " -> no swap"

            steps.append(info)
            step_id += 1

        steps.append(f"Array after pass {i + 1}: {a}")

        # if nothing happened, that means everything has sorted
        if not swapped:
            steps.append("No swaps in this pass. Already sorted. Stop early.")
            break

    steps.append(f"\nFinal sorted array: {a}")
    return steps, a

# run and check the bubble sort list resullt
def run_bubble_sort(text):
    try:
        nums = parse_input_list(text)
    except ValueError as e:
        return f"Input error: {e}", ""

    steps, result = bubble_sort_with_steps(nums)
    return "\n".join(steps), str(result)

# establish a project to run it in visualized UI
with gr.Blocks(title="Bubble Sort Visualizer") as demo:
    gr.Markdown("# Bubble Sort Visualizer\nEnter a list of integers to visualize bubble sort.")

    input_box = gr.Textbox(label="Input Your list", placeholder="e.g. 5, 3, 1, 4, 2")

    run_btn = gr.Button("Run")

    with gr.Row():
        steps_output = gr.Textbox(label="Steps", lines=20)
        result_output = gr.Textbox(label="Final result", lines=2)

    run_btn.click(
        fn=run_bubble_sort,
        inputs=input_box,
        outputs=[steps_output, result_output]
    )

if __name__ == "__main__":
    demo.launch()

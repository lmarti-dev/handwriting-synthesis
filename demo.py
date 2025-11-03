

from pathlib import Path

from hand import Hand
import os


from unidecode import unidecode


if __name__ == '__main__':
    hand = Hand()


    dirname =r"C:\Users\Moi4\Desktop\code\web\dxdt\mainwebsite\photos"
    tasks = os.listdir(dirname)

    
    tasks = [x for x in tasks if Path(dirname,x).is_dir()]

    for task in tasks:

        lines = [
           *unidecode(task).split(" ")
        ]
        print(f"Writing lines: {lines}")
        biases = [.8 for i in lines]
        # styles go from 0 to 12
        styles = [3 for i in lines]
        stroke_colors = ["black"]*len(lines)
        stroke_widths = [2]*len(lines)
        fout = Path(Path(__file__).parent,f'img/{task}.svg')
        print(f"Saving to {fout.as_posix()}")
        hand.write(
            filename=fout,
            lines=lines,
            biases=biases,
            styles=styles,
            stroke_colors=stroke_colors,
            stroke_widths=stroke_widths,
            alignment="center"
        )

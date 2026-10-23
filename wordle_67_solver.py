from pathlib import Path

script_dir = Path(__file__).parent

def determine_color(word_input, answer):
    word = word_input.upper()
    answer_list = list(answer.upper())

    color = [0, 0, 0, 0, 0]

    for i in range(5):
        if word[i] == answer_list[i]:
            color[i] = 2
            answer_list[i] = None

    for i in range(5):
        if color[i] == 0 and word[i] in answer_list:
            color[i] = 1
            answer_list[answer_list.index(word[i])] = None

    return color

pattern_67_0 = [
    [2, 2, 2, 0, 0],
    [2, 0, 1, 1, 1],
    [2, 2, 2, 0, 1],
    [2, 0, 2, 0, 1],
    [2, 2, 2, 0, 1],
    [0, 0, 0, 0, 1]
]

pattern_67_1 = [
    [1, 1, 1, 0, 0],
    [1, 0, 2, 2, 2],
    [1, 1, 1, 0, 2],
    [1, 0, 1, 0, 2],
    [1, 1, 1, 0, 2],
    [0, 0, 0, 0, 2]
]

pattern_67_2 = [
    [0, 0, 2, 2, 2],
    [2, 2, 2, 0, 2],
    [2, 0, 0, 0, 2],
    [2, 2, 2, 0, 2],
    [2, 0, 2, 0, 2],
    [2, 2, 2, 0, 0]
]

pattern_67_3 = [
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0]
]

pattern_67_4 = [
    [0, 0, 1, 1, 1],
    [2, 2, 2, 0, 1],
    [2, 0, 0, 0, 1],
    [2, 2, 2, 0, 1],
    [2, 0, 2, 0, 1],
    [2, 2, 2, 0, 0]
]

pattern_67_5 = [
    [0, 0, 2, 2, 2],
    [1, 1, 1, 0, 2],
    [1, 0, 0, 0, 2],
    [1, 1, 1, 0, 2],
    [1, 0, 1, 0, 2],
    [1, 1, 1, 0, 0]
]

answer = input("Answer (5 letters) = ")

if(len(answer) == 5):
    with open(script_dir/"word_list.txt", "r", encoding="utf-8") as file:
        word_list = [line.strip() for line in file if line.strip()]

    word_color = []
    for word in word_list:
        word_color.append([word, determine_color(word, answer)])

    for i in range(6):
        pattern_success = 0
        for color in globals()["pattern_67_" + str(i)]:
            for result in word_color:
                if color == result[1]:
                    print(result)
                    pattern_success += 1
                    break

        if pattern_success == 6:
            print(f"pattern {i} success")
        else:
            print(f"pattern {i} failed")
        
        print()
else:
    print("Answer must equal to 5 letters")

input("Press Enter to exit...")
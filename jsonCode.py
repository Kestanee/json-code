
import json

def open_json(path):
    with open(path, 'r') as json_data:
        datas = json.load(json_data)

    return datas

def json_process(datas):
    result = {}

    for d in datas:
        for question in d['questions']:
            question_number = question['num'].strip('.')
            answer = d['answers'].get(question_number)
            if answer:
                question['answers'] = answer

    result = datas
    return result

def eval_json(result):
    j_data = []
    for datas in result:
        for question in datas.get("questions", []):
            j_data.append(question)

    return j_data

def answer_pop(result):
    remove_answer = {}
    for d in result:
            d.pop('answers', None)  # 'answers' alanını sil

    remove_answer = result
    return remove_answer
def options_remove(remove_answer):
    new_data = []
    for question_data in remove_answer:
        print(question_data)

        new_question_data = {
            "num": question_data.get("num", ""),
            "question": question_data.get("question", ""),
            "answers": question_data.get("answers", "")
        }
        # options içindeki değerleri anahtar olarak kullanarak ekleyin
        options = question_data.get("options", {})
        for key, value in options.items():
            new_question_data[key] = value.strip()  # strip ile baştaki ve sondaki boşlukları temizle

        new_data.append(new_question_data)

    return new_data

def num(new_data):
    for i, datas in enumerate(new_data):
        datas['num'] = i + 1

    return new_data

def write_json(path, result):
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    open_path = "/home/furkan/PycharmProjects/json_xml_join/eval_json/tr_evaluation.json"
    write_path = "/home/furkan/PycharmProjects/json_xml_join/eval_json/news.json"
    datas = open_json(open_path)
    result = json_process(datas)
    remove_answer = answer_pop(result)
    j_data = eval_json(remove_answer)
    options_remove = options_remove(j_data)
    new_data = num(options_remove)
    write_json(write_path, new_data)

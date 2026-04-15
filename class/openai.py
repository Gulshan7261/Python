# import openai
# openai.api_key = "sk-"

Student = {
    "name":"Gulshan",
    "class":{
        "che":65
    }
}
new_dict = {"rahul":80}
Student.update(new_dict)
print(Student)
# print(Student.get("name"))
# print(Student["class"])

# student = { "name" : "Gulshan", "subject" : { "che":95, "math":62 } }
# print(student)

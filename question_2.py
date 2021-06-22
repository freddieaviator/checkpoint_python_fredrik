
def to_camel_case(text):
    try:
        text = text.split(" ")
        result = ""
        for word in text:
            result += word.capitalize()
        return result

    except Exception as e:
        return (f"Error: {e}")

print(to_camel_case("hello world"))
print(to_camel_case("My stRiNg"))
print(to_camel_case("tHis Is A tesT string"))

def to_snake_case(camel):
    try:
        result = [camel[0].lower()]
        if(" " in camel):
            raise ValueError("wrong format dude! Try again")
        else:
            for char in camel[1:]:
                if char in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                    result.append("_")
                    result.append(char.lower())
                else:
                    result.append(char)
            return str.join("",result)
    
    except Exception as e:
        return (f"Error: {e}")

print(to_snake_case("ThisIsASnakeTestString"))
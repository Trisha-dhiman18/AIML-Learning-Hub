letter = '''Dear <|Name|>, 
            You are selected! 
        <|Date|> '''
print(letter.replace("<|Name|>", "Vishal").replace("<|Date|>", "June 20, 2024"))
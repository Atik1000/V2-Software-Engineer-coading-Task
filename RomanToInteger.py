def roman_to_int(s):
    roman_numerals={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    result =0 
    for i in range(len(s)):
        current= roman_numerals[s[i]]
        next=roman_numerals[s[i+1]] if i<len(s)-1 else 0

        if current<next:
            result -=current
        else:
            result += current
    return result

roman_numerals="III"

integer_value=roman_to_int(roman_numerals)

print(integer_value)
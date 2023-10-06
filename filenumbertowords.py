def convert_number_to_words(number):
    # Define word equivalents for numbers
    units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
             'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    words = ''

    if number == 0:
        return 'Zero'

    # Convert number to words
    if number // 100 > 0:
        words += units[number // 100] + ' hundred '
        number %= 100

    if number // 10 == 1:
        words += teens[number % 10]
    else:
        words += tens[number // 10] + ' '
        words += units[number % 10]

    return words


file_path = 'numbers.txt'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read().strip()

# Convert the number to words
number = int(content)
words = convert_number_to_words(number)

# Update the file content with the converted number in words
with open(file_path, 'w') as file:
    file.write(f'{number} {words}')

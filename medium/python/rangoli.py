def rangoli(size):
  alphabet = [chr(char) for char in range(97, 123)]
  rangoli_list = []
  for letter in range(size):
    alpha_str = '-'.join(alphabet[letter:size])
    rangoli_list.append((alpha_str[::-1] + alpha_str[1:]).center(4 * size - 3, '-'))
  print('\n'.join(rangoli_list[:0:-1] + rangoli_list))

rangoli(6)
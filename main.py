name = input('username: \n')
password = input('Your password: \n')

pass_len = len(password)
pass_sign = pass_len * '*'

print(f'{name} your password {pass_sign} is {pass_len} digit long')

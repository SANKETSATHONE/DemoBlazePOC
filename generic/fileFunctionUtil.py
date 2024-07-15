import re
import time
import random
import os



class FileFunctionUtil:
    @staticmethod
    def get_random_string(string_len):
        # string of lower case alpha
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        # string of Upper case alpha
        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # concatenate both lowe_alpha + upper_alpha
        all_alpha = lower_alpha + upper_alpha
        string = ""
        for i in range(string_len):
            # getting single character from string in each iteration and add it to string
            string += random.choice(all_alpha)
        return string

    @staticmethod
    def verifyInputValueWithSpecificFormat(inp_value,
                                           regex_pattern):  # it takes two arguments first input value and regex pattern
        if re.fullmatch(regex_pattern, inp_value):
            return True
        else:
            return False

    @staticmethod
    def get_random_number(int_len):
        random_numbers = ""
        for i in range(int_len):
            random_numbers += str(random.randrange(0, 9))
        return random_numbers

    @staticmethod
    def get_random_string_with_number(int_len):
        string_with_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        result = ""
        for i in range(int_len):
            result += str(random.choice(string_with_numbers))
        return result

    # you can pass all gender as a string with comma seperation ex- "male, female,custom"
    @staticmethod
    def get_random_gender(genders):
        gender_list = genders.split(",")
        return random.choice(gender_list)

    # This function will get random date between two other provided date
    # You can pass start date-time, end date-time, in provided time format ex-"%m/%d/%/ 21:20 p
    @staticmethod
    def get_random_date(start, end, time_format):
        stime = time.mktime(time.strptime(start, time_format))
        etime = time.mktime(time.strptime(end, time_format))
        ptime = stime + random.random() * (etime - stime)
        return time.strftime(time_format, time.localtime(ptime))

    @staticmethod
    def getRandomPassword():
        lower_alpha = "abcdefghijklmnopqrstuvwxyz"
        upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digit = "1234567890"
        symbol = "!@#$%^&* ?."
        password = ""
        n = random.randint(2, 3)
        for i in range(n):
            password = password + random.choice(lower_alpha)
            password = password + random.choice(upper_alpha)
            password = password + random.choice(digit)
            password = password + random.choice(symbol)
        return password

    @staticmethod
    def get_dynamic_path(project_name):
        create_path = ""
        root_dir = os.path.abspath(os.curdir)
        split_dir = root_dir.split("\\")
        name = ""
        for list_value in split_dir:
            if list_value == project_name:
                name = list_value
                break
            create_path = create_path + "\\" + list_value
        create_path = create_path + "\\" + name
        final_path = create_path[1::]
        return final_path

    @staticmethod
    def make_dir_for_current_test_name(folder):
        tc = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        dir_name = f"{FileFunctionUtil.get_dynamic_path("DemoBlazePOC")}\\everyStepScreenshot\\{folder}\\{tc}"
        value = os.path.isdir(dir_name)
        if not value:
            os.mkdir(dir_name)
            return dir_name



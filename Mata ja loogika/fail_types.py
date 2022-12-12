"""File operations."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(f"{filename}") as f:
        string = f.read()
    return string


def read_file_contents_to_list(filename: str) -> list:
    """
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    line_list = []
    with open(f"{filename}") as f:
        for line in f:
            new_line = line.replace("\n", "")
            line_list.append(new_line)
    return line_list


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    result = []
    with open(f"{filename}") as f:
        for row in csv.reader(f):
            result.append(row)
    return result



def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    with open(f"{filename}", "w") as f:
        f.write(contents)


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    with open(f"{filename}", "w") as f:
        for line in lines:
            f.write(line)


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(f"{filename}", "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    date_list = []
    temp_date_list = []
    new_date_list = []
    town_list = []
    temp_town_list = []
    new_town_list = []
    data_list = []
    temp_list = []

    with open(dates_filename) as f:
        for line in f:
            date_list.append(line)
    f.close()

    for i in range(len(date_list) - 1):
        date_list[i] = date_list[i].strip()

    for line in date_list:
        temp_date_list.append(line.split(":"))

    with open(towns_filename) as f:
        for line in f:
            town_list.append(line)
    f.close()

    for i in range(len(town_list) - 1):
        town_list[i] = town_list[i].strip()

    for line in town_list:
        temp_town_list.append(line.split(":"))

    for lists in temp_town_list:
        temp_list.append(lists[-1])

    for element in temp_list:
        list_element = []
        list_element.append(element)
        new_town_list.append(list_element)

    data_list.append(["name", "town", "date"])
    for name in names_list:
        row = [name]
        if name in town_dict:
            row.append(town_dict[name])
        else:
            row.append("-")
        if name in date_dict:
            row.append(date_dict[name])
        else:
            row.append("-")
        data.append(row)
    data_list = new_date_list + new_town_list
    print(data_list)

    with open(csv_output_filename, "w") as output:
        writer = csv.writer(output)
        for row in data_list:
            writer.writerow(row)
    print(temp_town_list)
    print(temp_date_list)
    print(temp_town_list)
print(merge_dates_and_towns_into_csv("dates.txt", "towns.txt", "data.csv"))
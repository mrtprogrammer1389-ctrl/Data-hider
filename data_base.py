import pickle as pk
import os


class Hider:

    def __init__(self):

        self.title = "a program for hiding data"
        self.password = "MRT_data"
        self.path = os.getcwd()
        self.data_base = str(self.path) + "\\data base"

        if not os.path.exists(self.data_base):

            os.mkdir(self.data_base)

    def hide(self, file_path, save_name):

        with open(str(file_path), "rb") as F:

            file_data = F.read()

            F.close()

        data = {"file_data": file_data}

        try:

            with open(str(self.data_base) + f"\\{save_name}.dat", "wb") as F:

                F.close()
        except:
            pass

        with open(str(self.data_base) + f"\\{save_name}.dat", "ab") as F:

            pk.dump(data, F)

            F.close()

    def group_hide(self, folder_path):

        try:

            files = list(os.listdir(str(folder_path)))

            for i in files:

                file_path = folder_path + f"\\{i}"

                name = str(i).split(".")[0] + f"({str(i).split('.')[1]})"

                self.hide(file_path, name)

            return f"{len(files)} files hided by group hiding"

        except:

            return "diractory not found"

    def random_load(self, items, name_feature):

        data_list = os.listdir(self.data_base)

        if name_feature not in [None, ""]:

            target_list = [i for i in data_list if name_feature in i]

        else:

            target_list = data_list

        target_list = list(set(target_list))

        counter = int(items)

        for i in target_list:

            if counter == 0:

                break

            name = str(i).split(".")[0]

            if "(" in i:

                format = str(i).split("(")[1]
                format = format.split(")")[0]
                self.load(name, format)

            else:

                format = "mp4"

                self.load(name, format)

            counter = counter - 1

    def get_list(self):

        save_list = os.listdir(self.data_base)

        file_names = [i.replace(".dat", "") for i in save_list]

        return file_names

    def load(self, name, format):

        names = self.get_list()

        if not str(name) in names:

            return "file not found"

        with open(str(self.data_base) + f"\\{name}.dat", "rb") as F:

            data = pk.load(F)["file_data"]

            F.close()

        try:

            with open(str(os.getcwd()) + f"\\{name}.{format}", "wb") as F:

                F.close()

        except:
            pass

        with open(str(os.getcwd()) + f"\\{name}.{format}", "ab") as F:

            F.write(data)

            F.close()


mrt = Hider()

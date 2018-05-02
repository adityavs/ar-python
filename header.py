class Header(object):
    def __init__(self, file_identifier = None, modification_time = -1, owner_id = -1, group_id = -1, file_mode = -1, file_size = -1):
        self.file_identifier = file_identifier
        self.modification_time = modification_time
        self.owner_id = owner_id
        self.group_id = group_id
        self.file_mode = file_mode
        self.file_size = file_size
        self.ending = "\x60\x0a"

    def get_file_identifier():
        return self.file_identifier

    def get_modification_time():
        return self.modification_time

    def get_owner_id():
        return self.owner_id

    def get_group_id():
        return self.group_id

    def get_file_mode():
        return self.file_mode

    def get_file_size():
        return self.file_size

    def parse_header(data):
        file_identifier = data[:16].rstrip()
        modification_time = int(data[16:28].rstrip())
        owner_id = int(data[28:34].rstrip())
        group_id = int(data[34:40].rstrip())
        file_mode = data[40:48].rstrip()
        file_size = int(data[48:58].rstrip())

        return (Header(file_identifier, modification_time, owner_id, group_id, file_mode, file_size), data[60:])

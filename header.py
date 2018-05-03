class Header(object):
    def __init__(self, file_identifier = None, modification_time = -1, owner_id = -1, group_id = -1, file_mode = -1, file_size = -1, ending = None):
        self._file_identifier = file_identifier
        self._modification_time = modification_time
        self._owner_id = owner_id
        self._group_id = group_id
        self._file_mode = file_mode
        self._file_size = file_size
        self._ending = ending

    def get_file_identifier(self):
        return self._file_identifier

    def get_modification_time(self):
        return self._modification_time

    def get_owner_id(self):
        return self._owner_id

    def get_group_id(self):
        return self._group_id

    def get_file_mode(self):
        return self._file_mode

    def get_file_size(self):
        return self._file_size

    def get_ending(self):
        return self._ending

    def parse_header(data):
        file_identifier = data[:16].rstrip()
        modification_time = int(data[16:28].rstrip())
        owner_id = int(data[28:34].rstrip())
        group_id = int(data[34:40].rstrip())
        file_mode = data[40:48].rstrip()
        file_size = int(data[48:58].rstrip())
        ending = data[58:60]

        return (Header(file_identifier, modification_time, owner_id, group_id, file_mode, file_size, ending), data[60:])

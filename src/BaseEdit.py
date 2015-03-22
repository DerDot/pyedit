class BaseEdit(object):
    
    def __init__(self):
        self.search_string = None
        self.edit_id = "base"
    
    def _search(self, search_string):
        raise NotImplementedError
    
    def set_dict(self, spell_dict):
        return

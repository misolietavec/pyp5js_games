import json

from pyp5js.config.fs import PYP5JS_FILES

TRANSCRYPT_INTERPRETER = 'transcrypt'
PYODIDE_INTERPRETER = 'pyodide'

class SketchConfig:

    @classmethod
    def from_json(cls, json_file_path):
        with open(json_file_path) as fd:
            config_data = json.load(fd)
            return cls(**config_data)

    def __init__(self, interpreter):
        self.interpreter = interpreter

    def get_index_template(self):
        index_map = {
            TRANSCRYPT_INTERPRETER: PYP5JS_FILES.transcrypt_index_html,
            PYODIDE_INTERPRETER: PYP5JS_FILES.pyodide_index_html,
        }
        return index_map[self.interpreter]

    def write(self, fname):
        with open(fname, "w") as fd:
            data = {"interpreter": self.interpreter}
            json.dump(data, fd)

    def get_target_js_template(self):
        target_map = {
            TRANSCRYPT_INTERPRETER: PYP5JS_FILES.transcrypt_target_sketch_template,
            PYODIDE_INTERPRETER: PYP5JS_FILES.pyodide_target_sketch_template,
        }
        return target_map[self.interpreter]

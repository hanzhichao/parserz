import re
import yaml
from jsonpath import jsonpath
from string import Template


class SimpleParser(object):
    def parse(self, data: (str, list, dict), context: dict):
        assert isinstance(data, (str, list, dict)), 'data should be str or list or dict type'
        if isinstance(data, str):
            return Template(data).safe_substitute(context)
        data_str = yaml.safe_dump(data, default_flow_style=False)
        parsed_data_str = Template(data_str).safe_substitute(context)
        return yaml.safe_load(parsed_data_str)


class DotParzer(object):
    VAR_PARTTERN = re.compile(r'\$\w+?[\w.]*\w*')

    @staticmethod
    def dot_get(expr: str, context: dict):
        value = context
        dots = expr.strip('$').split('.')
        for dot in dots:
            if hasattr(value, dot):
                value = getattr(value, dot)
                continue
            if dot.isdigit():
                dot = int(dot)
            try:
                value = value[dot]
            except Exception as ex:
                return expr
            if callable(value):
                value = value()
        return value

    def parse(self, data: (str, list, dict), context: dict):
        """解析$变量"""
        def repr_func(matched):
            if not matched:
                return
            expr = matched.group(0)
            print('matched', expr)
            value = self.dot_get(expr, context)
            if isinstance(value, str) and not isinstance(data, str):
                return f'"{value}"'
            return f'{value}'
        patten = self.VAR_PARTTERN
        if isinstance(data, str):
            return re.sub(patten, repr_func, data)

        data_str = yaml.safe_dump(data)
        parsed_data_str = re.sub(patten, repr_func, data_str)
        parsed_data = yaml.safe_load(parsed_data_str)
        return parsed_data


class JsonPathParser(object):
    VAR_PARTTERN = re.compile(r'\$\w+?[\w.]*\w*')

    def jsonpath(self, expr: str, context: dict):
        result = jsonpath(context, expr)
        return expr if result is False else result[0] if result else None

    def parse(self, data: (str, list, dict), context: dict):
        def repr_func(matched):
            if not matched:
                return
            expr = matched.group(0)
            print('matched', expr)
            value = self.jsonpath(expr.replace('$', '$.'), context)
            if isinstance(value, str) and not isinstance(data, str):
                return f'"{value}"'
            return f'{value}'
        patten = self.VAR_PARTTERN
        if isinstance(data, str):
            return re.sub(patten, repr_func, data)

        data_str = yaml.safe_dump(data)
        parsed_data_str = re.sub(patten, repr_func, data_str)
        parsed_data = yaml.safe_load(parsed_data_str)
        return parsed_data


parser = DotParzer()
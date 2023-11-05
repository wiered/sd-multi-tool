from core import read_csv

class Style:
    def __init__(self, style):
        self._name: str = style[0]
        self._prompt: str = style[1]
        self._negative_prompt: str = style[2]
        

    @property
    def name(self):
        return self._name


    @property
    def prompt(self):
        return self._prompt
    

    @property
    def negative_prompt(self):
        return self._negative_prompt
    

    @name.setter
    def name(self, value) -> str:
        if len(value) < 1:
            raise ValueError
        
        self._name = value

    
    @prompt.setter
    def prompt(self, value):
        self._prompt = value


    @negative_prompt.setter
    def negative_prompt(self, value):
        self._negative_prompt = value


    def __eq__(self, other: str):
        return self.name == other


    def __repr__(self):
        return f"self.name: {self.name}, self.prompt: {self.prompt}, self.negative_prompt: {self.negative_prompt}"


class Category:
    def __init__(self, name):
        if not name:
            raise ValueError
        
        self._name = name
        self._styles: list[Style] = []

    
    @property
    def name(self) -> str:
        """Category name

        Returns:
            str
        """
        return self._name


    @property
    def styles(self) -> list[Style]:
        """styles

        Returns:
            list[Style]: list of styles
        """
        return self._styles


    @name.setter
    def name(self, value: str):
        """Category name setter.

        Args:
            value (str): _description_

        Raises:
            ValueError: _description_
        """
        if not type(value) is str:
            raise ValueError("Value must be a string")
        
        if len(value) < 1:
            raise ValueError("Value lenght must be > 1")
        
        self._name = value


    @styles.setter
    def styles(self, value):
        """Styles setter(doing nothing?)

        Args:
            value: just value, any value
        """
        return


    def is_style_exist(self, style_name: str) -> bool:
        """Returns true if the style exists int this category

        Args:
            style_name (str): _description_

        Returns:
            bool: _description_
        """
        for style in self._styles:
            if style == style_name:
                return True
            
        return False

    
    def append(self, style: Style):
        """addpend style to style list

        Args:
            style (Style): Style

        Raises:
            ValueError: raise if {style} type is not Style
        """
        if not type(style) == Style:
            raise ValueError

        self._styles.append(style)
    

    def remove(self, style_name: str):
        """Remove a style from category

        Args:
            style_name (str): style name
        """
        if not self.is_style_exist(style_name):
            return 

        for style in self._styles:
            if style == style_name:
                self._styles.remove(style)
    

    def clear(self):
        """clear styles of category
        """
        self._styles: list[Style] = []


    def find_by_name(self, _style) -> Style:
        """Finds a style by name. 
            I'm trying always returning a Style object, 
            so there will not be some problems with None values.

        Args:
            name (str): style name

        Returns:
            Style: Style
        """
        for style in self._styles:
            if style == _style:
                return style
        
        return Style(["", "Probably style not found", ""])


class StylesList:
    def __init__(self):
        self._categories: list[Category] = []


    @property
    def categories(self) -> list[Category]:
        """returns a list of categories

        Returns:
            list[Category]
        """
        return self._categories


    @property
    def last_category(self) -> Category:
        """Returns the last category

        Returns:
            Category: last category
        """
        return self.categories[len(self.categories)-1]
    

    @property
    def length(self) -> int:
        """count of styles

        Returns:
            int: length of the style_list
        """
        length = 0
        for category in self.categories:
            length += len(category.styles)

        return length + len(self.categories)


    @categories.setter
    def categories(self, value):
        """categories setter

        Args:
            value (list): categories list
        """
        self._categories = value


    def is_style_exists(self, style_name: str) -> bool:
        """Returns true if style exists

        Args:
            style_name (str): style name

        Returns:
            bool: true if style exists else false
        """
        for category in self.categories:
            if category.is_style_exist(style_name):
                return True

        return False
    

    def append(self, style: Style):
        """Add style to last category

        Args:
            style (Style): style to append

        TODO:
            add style to any category
        """
        self.last_category.append(style)

    def remove(self, style_name: str):
        """Remove style

        Args:
            style_name (str): style name
        """
        for category in self.categories:
            if category.is_style_exist(style_name):
                category.remove(style_name)
        
        return


    def read_from_csv(self, csv_filename: str):
        """Read style from CSV file

        Args:
            csv_filename (str): path to CSV file
        """
        styles = read_csv(csv_filename)
        categories = 0
        for style in styles:
            if len(style[0]) == 0: # it is delimiter
                continue
            elif len(style[1]) == 0 and len(style[2]) == 0: # it is category
                categories += 1
        
        print(categories)
        if categories == 0:
            self.categories.append(Category('Default'))

        for style in styles:
            if len(style[0]) == 0: # it is delimiter
                continue
            elif len(style[1]) == 0 and len(style[2]) == 0: # it is category
                category = Category(style[0])
                self.categories.append(category)
            else: # it is a style
                _style = Style(style)
                self.categories[len(self.categories)-1].append(_style)
    

    def find_by_name(self, name) -> Style:
        """Finds a style by name. 
            I'm trying always returning a Style object, 
            so there will not be some problems with None values.

        Args:
            name (str): style name

        Returns:
            Style: Style
        """
        for category in self.categories:
            style = category.find_by_name(name)
            if len(style.name) != 0: 
                return style
                
        return Style(["style_not_found_error", "Probably style not found", ""])
    

    def save_style(self, style_name: str, prompt: str, negative_prompt: str):
        """Save style

        Args:
            style_name (str): style name
            prompt (str): style prompt
            negative_prompt (str): style negative prompt
        """
        if not self.is_style_exists(style_name):
            return

        style = self.find_by_name(style_name)
        style.prompt = prompt
        style.negative_prompt = negative_prompt


    def clear(self):
        """Clear all styles and categories
        """
        self._categories: list[Category] = []

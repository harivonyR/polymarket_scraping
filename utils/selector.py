"""
SAFE SELECTOR : 
    + manage selection error or missing value

"""

def get_one(find_fn, default=""):
        try:
            el = find_fn()
            return el.text if el else default
        except:
            return default

def get_attr(find_fn, attr, default=""):
    try:
        el = find_fn()
        return el.get(attr, default) if el else default
    except:
        return default

def get_list(find_fn):
    try:
        els = find_fn()
        return [e.text for e in els] if els else []
    except:
        return []
    
"""
Multi Class Selector : 
    + custom selector that return only element with specific class list

"""  
    
def find_with_all_classes(soup, classes):
    """ return all elements that contain all classes """
    return soup.find_all(
        lambda tag: tag.has_attr("class") and all(c in tag["class"] for c in classes)
    )

def find_with_classes(soup, classes):
    """ return first elements that contain all classes """
    return soup.find(
        lambda tag: tag.has_attr("class") and all(c in tag["class"] for c in classes)
    )
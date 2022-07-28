from json2html import *

def html_conv(content):
    import json 
    from draftjs_exporter.html import HTML
    config = {} 
    exporter = HTML(config)
    """
    pip==22.2,
    Python==3.10.5,
    json2html==1.3.0,
    draftjs_exporter==5.0.0
    """
    try:
        try: # for "{\\\"blocks\\\":[{\\\"k
            value1 = content.replace('\\','')
            value1 = value1.replace('Â· ','')
            value2 = json.loads('{}'.format(value1))
            html = exporter.render(value2)
        except: # for coming through files
            value1 = content.replace('\\','')
            value1 = value1.replace('Â· ','')
            value2 = json.loads('{}'.format(value1))
            htm = ""
            for i in value2['blocks']:
                key, text, type, depth = i['key'], i['text'], i['type'], i['depth']
                inlineStyleRanges, entityRanges, data = i['inlineStyleRanges'], i['entityRanges'], i['data']
                htm = htm + exporter.render({
                    'entityMap': {},
                    'blocks': [{
                        'key': key,
                        'text': text,
                        'type': type,
                        'depth': depth,
                        'inlineStyleRanges': {},
                        'entityRanges': entityRanges,
                        'data': data}]})
            html = htm
    except: # for '{"blocks":[{"key":"sbbp","text":" or blank or anything
        value1 = str(content).replace('\\','')
        value1 = value1.replace('Â· ','')
        html = value1
    return html

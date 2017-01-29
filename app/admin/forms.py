
def generateForms(form):
	generated = []
	for field in form:
		generated.append(getFields(field))
	return generated

def getFields(field):
	text = """<div class="col-md-5"> <div class="form-group label-floating"> <label class="control-label">%s</label <input type="text" class="%s" name="%s"> </div> </div>""" % (field['label'], field['class'], field['name']),
	
	Ftype = field['type']
	return {
		'text':text,
		'file':'This is B'
		}[Ftype]

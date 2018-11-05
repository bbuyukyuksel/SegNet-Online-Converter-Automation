import mechanize
from base64 import b64decode
import os
class getSegnetDemo:
    _FILENAME = None
    _URL = None
    _REQUEST_URL = 'http://mi.eng.cam.ac.uk/projects/segnet/#demo'
    _SHOW_LOGS = False

    def __init__ (self, filename=None, url=None, log=None):

        if log:
            self._SHOW_LOGS = log

        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)  # ignore robots
        self.br.open(self._REQUEST_URL)

        self.br.form = self.br.forms()[0]
        self.br.set_all_readonly(False)

        if filename:
            self._FILENAME = "result_" + filename[::-1].split('/')[0][::-1]
            self.log("{:<20} : {:_>40}".format("Filename",filename))
            self.br.form.add_file(open(filename, 'rb'), 'image/jpeg', filename)
        elif url:
            urlName = url[::-1].split('/')[0][::-1]
            self._FILENAME = "result_" + urlName
            self.log("{:<20} : {:_>40}".format("URL Name", urlName))
            self.br["imageURL"] = url
        else:
            print "Error"
            exit()

    def start(self):

        self.response = self.br.submit()
        self.content = self.response.read()
        #print "Response" + self.content
        self.br.close()
    def getContent(self):
        return self.content

    def getBase64Image(self):
        startIndex = self.content.find('("result_image").setAttribute( "src", "')
        first = '"data:image/png;base64,'
        last = '" ); </script><script type="text/javascript"> show_display_form();</script>'
        self.base64Image = self.find_between(self.content[startIndex:], first, last)
        self.log("{:<20} : {:_>40}".format("Base64Image", self.base64Image))

    def saveBase64Image(self,path=None):
        imgdata = b64decode(self.base64Image)
        filename = self._FILENAME  # I assume you have a way of picking unique filenames
        if path:
            try:
                os.mkdir(path)
            except:
                pass
            filename = path + filename
        with open(filename, 'wb') as f:
            f.write(imgdata)
        self.log('{:<20} : {:_>40}'.format("Saved File",self._FILENAME))

    def find_between(self, s, start, end):
        return (s.split(start))[1].split(end)[0]

    def log(self,*args):
        if self._SHOW_LOGS:
            print(args)
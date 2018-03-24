# -*- coding:utf-8 -*-

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []



    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # python默认的编码时ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td width=300px>%s</td>" % data['url'])
            fout.write("<td width=200px>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td cols=100>%s</td>" % data['summary'].encode('utf-8'))

            fout.write("</tr>")


        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
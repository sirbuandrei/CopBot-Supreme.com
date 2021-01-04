import gui, bot, sys

IT = []
processes = []


class User(object):
    def __init__(self, name, email, tel, address, city, postcode, country, card_type, card_number, card_month,
                 card_year, card_cvv):
        self.name = name
        self.email = email
        self.tel = tel
        self.address = address
        self.city = city
        self.postcode = postcode
        self.country = country
        self.card_type = card_type
        self.card_number = card_number
        self.card_month = card_month
        self.card_year = card_year
        self.card_cvv = card_cvv

    def __repr__(self):
        return '(%s %s %s %s %s)' % (self.name, self.address, self.country, self.card_type, self.card_cvv)


MyUser = User("", "", "", "", "", "", "", "", "", "", "", "")

country = {
    'UK': 'GB',
    'UK (N. IRELAND)': 'NB',
    'AUSTRIA': 'AT',
    'BELARUS': 'BY',
    'BELGIUM': 'BE',
    'BULGARIA': 'BG',
    'CROATIA': 'HR',
    'CZECH REPUBLIC': 'CZ',
    'DENMARK': 'DK',
    'ESTONIA': 'EE',
    'FINLAND': 'FI',
    'FRANCE': 'FR',
    'GERMANY': 'DE',
    'GREECE': 'GR',
    'HUNGARY': 'HU',
    'ICELAND': 'IS',
    'IRELAND': 'IE',
    'ITALY': 'IT',
    'LATVIA': 'LV',
    'LITHUANIA': 'LT',
    'LUXEMBOURG': 'LU',
    'MONACO': 'MC',
    'NETHERLANDS': 'NL',
    'NORWAY': 'NO',
    'POLAND': 'PL',
    'PORTUGAL': 'PT',
    'ROMANIA': 'RO',
    'RUSSIA': 'RU',
    'SLOVAKIA': 'SK',
    'SLOVENIA': 'SI',
    'SPAIN': 'ES',
    'SWEDEN': 'SE',
    'SWITZERLAND': 'CH',
    'TURKEY': 'TR'
}

size= {
    '0': 'small',
    '1': 'medium',
    '2': 'large',
    '3': 'xlarge'
}

card = {
    'Visa': 'visa',
    'American Express': 'american_express',
    'Mastercard': 'master',
    'Solo': 'solo'
}


class MyQtApp(gui.Ui_MainWindow, gui.QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("BlazeBot")
        self.buying_list.resizeColumnToContents(0)
        self.save_btn.clicked.connect(self.get_user_info)
        self.add_item.clicked.connect(self.get_item_info)
        self.buy_items.clicked.connect(self.buyitms)


    def get_user_info(self):
        name = self.name_lineEdit.text()
        print(name)
        #MyUser = User(self.name_lineEdit.text(), self.email_lineEdit.text(), self.tel_lineEdit.text(), self.address_lineEdit.text(), self.city_lineEdit.text(), self.postcode_lineEdit.text(), country[self.coutry_comboBox.currentText()], card[self.card_type_comboBox.currentText()], self.card_number_lineEdit.text(), self.card_month_comboBox.currentText(), self.card_year_comboBox.currentText(), self.cvv_lineEdit.text())
        #print(MyUser)


    def get_item_info(self):
        IT.append(bot.item(self.comboBox.currentText(), self.kw1_lineEdit.text(), self.kw2_lineEdit.text(),
                           self.colour_lineEdit.text(), int(self.size_combo.currentIndex())))

        showx = IT[-1].coat + " (" + IT[-1].KW1 + ", " + IT[-1].KW2 + ") " + IT[-1].colour + " " + size[str(IT[-1].size)]
        print(showx)
        self.comboBox.setCurrentIndex(0)
        self.kw1_lineEdit.clear()
        self.kw2_lineEdit.clear()
        self.colour_lineEdit.clear()
        self.size_combo.setCurrentIndex(0)
        print(IT)

    def buyitms(self):
        for itm in IT:
            p = bot.multiprocessing.Process(target=itm.buy)
            p.start()
            processes.append(p)

        for process in processes:
            process.join()


if __name__ == "__main__":
    app = gui.QtWidgets.QApplication(sys.argv)
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()

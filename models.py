class Account:
    def __init__(self, number, agency, balance, limit):
        self.number = number
        self.agency = agency
        self.balance = balance
        self.limit = limit


class Feature:
    def __init__(self, icon, description):
        self.icon = icon
        self.description = description


class Card:
    def __init__(self, number, limit):
        self.number = number
        self.limit = limit


class News:
    def __init__(self, icon, description):
        self.icon = icon
        self.description = description


class User:
    def __init__(self, name, account, features, card, news):
        self.name = name
        self.account = account
        self.features = features
        self.card = card
        self.news = news

class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not 5 <= len(title) <= 50:
            raise ValueError("Article title must be between 5 and 50 characters, inclusive")
        self.author = author
        self.magazine = magazine
        self._title = title
        self.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"Article(title='{self.title}')"


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        topics = [article.magazine.category for article in self._articles]
        return list(set(topics)) if topics else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        return [author for author, count in author_counts.items() if count > 2]

    def __repr__(self):
        return f"Author(name='{self.name}')"


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Magazine name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Magazine name must be between 2 and 16 characters, inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Magazine category must be a string")
        if not value:
            raise ValueError("Magazine category cannot be empty")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1
        return [author for author, count in author_counts.items() if count > 2] if len(self._articles) > 2 else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))

    def __repr__(self):
        return f"Magazine(name='{self.name}', category='{self.category}')"

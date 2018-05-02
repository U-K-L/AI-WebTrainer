class PageManager:
    Pages= {}

    def StoreHtml(self, Page):
        PageManager.Pages.update({Page.fileName, Page.key})
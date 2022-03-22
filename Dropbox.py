import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BESDqIB05iRqIUHoAjfxvHc2oSe37Zwj2cabZnOpHyHuQK05SHDfels0K1oNEQnSyEVTmK1vgBWQKnkZgpSuqDo2ZmpRkDz2Qc49w5pagMK_3W_UWoHpyTAZflxHk480WbvKw2A'
    transferData = TransferData(access_token)

    file_from = 'D://1_Nirvan//whitehat.jr//Python//C-101//test.txt'# Add full path here 
    file_to = '/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("done")
if __name__ == '__main__':
    main()
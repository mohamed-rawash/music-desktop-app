pyrcc5 forms\app_resource.qrc -o app_resource_rc.py
pyuic5 forms\song_form.ui -o views\song_view.py
pyuic5 forms/media_playlist_form.ui -o views\media_playlist_view.py
pyuic5 forms/singer_info_form.ui -o views\singer_info_view.py
pyuic5 forms/singer_page_form.ui -o views\singer_page_view.py
pyuic5 forms/add_singer_dialog_form.ui -o views\add_singer_dialog_view.py
pyuic5 forms/main_page_form.ui -o views\main_page_view.py
pyuic5 forms/main_app_form.ui -o views\main_app_view.py
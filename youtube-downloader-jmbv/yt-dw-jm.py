from pytube import YouTube, Playlist
from os import path

# region test code

# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# list_url = "https://www.youtube.com/playlist?list=PLpjXzIK4leLynAEagpDMpREgMt2uM6rQz"

# yt = YouTube(
#     video_url,
#     use_oauth=True,
#     allow_oauth_cache=True,
# )

# pl = Playlist(list_url)

# print(pl)

# Descargar el vídeo de mayor calidad
# yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download()

# Descargar el audio de mayor calidad
# yt.streams.filter(only_audio=True).order_by("abr").desc().first().download()

# Descargar todos los vídeos de una lista


# for stream in yt.streams.filter(only_audio=True).order_by("abr").desc():
#     print(stream)

# endregion


# region functions


def descargar_video(url, dir=None, name=None):

    yt = YouTube(
        url,
        use_oauth=True,
        allow_oauth_cache=True,
    )

    yt.streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download(output_path=dir, filename=f"{name}.mp4")


def descargar_audio(url, dir=None, name=None):
    yt = YouTube(
        url,
        use_oauth=True,
        allow_oauth_cache=True,
    )

    yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(
        output_path=dir, filename=f"{name}.mp3"
    )


def descargar_video_playlist(url, dir=None, folder_name=None):
    pl = Playlist(url)

    if folder_name is None:
        folder_name = pl.title.replace(" ", "_")
    else:
        folder_name = folder_name.replace(" ", "_")

    if dir is None:
        dir = path.join(path.abspath(path.dirname(__file__)), folder_name)
    else:
        dir = path.join(dir, folder_name)

    for video in pl.videos:
        try:
            descargar_video(
                f"https://www.youtube.com/watch?v={video.video_id}",
                dir,
                video.title.replace(" ", "_"),
            )
        except:
            # keep only alphanumeric values and spaces in video.title
            nuevo_nombre = "".join([c for c in video.title if c.isalnum() or c == " "])
            descargar_video(
                f"https://www.youtube.com/watch?v={video.video_id}",
                dir,
                nuevo_nombre,
            )
        print(
            f"({list(pl.videos).index(video) + 1}/{len(list(pl.videos))}) --> Descargado {video.title}"
        )


def descargar_audio_playlist(url, dir=None, folder_name=None):
    pl = Playlist(url)
    if folder_name is None:
        folder_name = pl.title.replace(" ", "_")
    else:
        folder_name = folder_name.replace(" ", "_")
    if dir is None:
        dir = path.join(path.abspath(path.dirname(__file__)), folder_name)
    else:
        dir = path.join(dir, folder_name)
    for video in pl.videos:
        try:
            descargar_audio(
                f"https://www.youtube.com/watch?v={video.video_id}",
                dir,
                video.title.replace(" ", "_"),
            )
        except:
            # keep only alphanumeric values and spaces in video.title
            nuevo_nombre = "".join([c for c in video.title if c.isalnum() or c == " "])
            descargar_audio(
                f"https://www.youtube.com/watch?v={video.video_id}",
                dir,
                nuevo_nombre,
            )
        print(
            f"({list(pl.videos).index(video) + 1}/{len(list(pl.videos))}) --> Descargado {video.title}"
        )


# endregion


# region function example calls

# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# list_url = "https://www.youtube.com/playlist?list=PLpjXzIK4leLynAEagpDMpREgMt2uM6rQz"

# descargar_video(video_url)
# descargar_video(video_url, dir=rf"C:\Users\hp\Downloads")
# descargar_video(video_url, dir=rf"C:\Users\hp\Downloads", name="prueba_video")

# descarregar_audio(video_url)
# descarregar_audio(video_url, dir=rf"C:\Users\hp\Downloads")
# descarregar_audio(video_url, dir=rf"C:\Users\hp\Downloads", name="prueba_audio")

# descargar_video_playlist(list_url)
# descargar_video_playlist(list_url, dir=rf"C:\Users\hp\Downloads")
# descargar_video_playlist(list_url, dir=rf"C:\Users\hp\Downloads", folder_name="prueba_carpeta_videos")

# descargar_audio_playlist(list_url)
# descargar_audio_playlist(list_url, dir=rf"C:\Users\hp\Downloads")
# descargar_audio_playlist(list_url, dir=rf"C:\Users\hp\Downloads", folder_name="prueba_carpeta_audios")

# endregion

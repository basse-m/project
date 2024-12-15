# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo[height<=1080]+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'bestvideo[height<=480]+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             video_url = info.get('url', None)
#             if not video_url:
#                 messagebox.showerror("خطأ", f"لا توجد بيانات لدقة {resolution}.")
#             else:
#                 webbrowser.open(video_url)

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# # واجهة المستخدم
# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()





# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             video_url = info.get('url', None)
#             if not video_url:
#                 messagebox.showerror("خطأ", f"لا توجد بيانات لدقة {resolution}.")
#             else:
#                 webbrowser.open(video_url)

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")


# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()







# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}

        
#         if resolution == "high":
#             ydl_opts = {'format': 'best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          
#             info = ydl.extract_info(url, download=False)

           
#             if 'formats' in info:
#                 formats = info['formats']
                
#                 best_video_url = None
#                 for f in formats:
#                     if f.get('format_note') == 'hd720':  
#                         best_video_url = f.get('url')
#                         break
#                     elif f.get('format_note') == '360p': 
#                         best_video_url = f.get('url')

#                 if best_video_url:
#                     webbrowser.open(best_video_url)
#                 else:
#                     messagebox.showerror("خطأ", "لم يتم العثور على رابط فيديو صالح.")

#             else:
#                 messagebox.showerror("خطأ", "لا توجد بيانات للفيديو.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")


# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()





# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}

        
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            
#             info = ydl.extract_info(url, download=False)

            
#             if 'formats' in info:
#                 formats = info['formats']
#                 best_video_url = None

                
#                 if resolution == "audio":
#                     for f in formats:
#                         if f.get('acodec') and f.get('format_note') == 'audio only':
#                             best_video_url = f.get('url')
#                             break

                
#                 elif resolution in ["high", "low"]:
#                     for f in formats:
#                         if f.get('format_note') and 'video' in f.get('format_note'):
#                             best_video_url = f.get('url')
#                             break

#                 if best_video_url:
#                     webbrowser.open(best_video_url)
#                 else:
#                     messagebox.showerror("خطأ", "لم يتم العثور على رابط فيديو أو صوت صالح.")

#             else:
#                 messagebox.showerror("خطأ", "لا توجد بيانات للفيديو.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")


# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()




# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             # استخراج جميع المعلومات المتاحة حول الفيديو
#             info = ydl.extract_info(url, download=False)

#             # تحقق من أن الفيديو يحتوي على رابط صالح
#             if 'formats' in info:
#                 formats = info['formats']
#                 available_formats = [f"{f.get('format_note', 'Unknown')} - {f.get('url')}" for f in formats]
#                 print("\nAvailable formats and URLs:")
#                 for format_str in available_formats:
#                     print(format_str)

#                 best_video_url = None
#                 best_audio_url = None

#                 # البحث عن أفضل دقة وجودة صوت
#                 for f in formats:
#                     if f.get('vcodec') and f.get('acodec'):  # فيديو مع صوت
#                         if resolution == "high" and best_video_url is None:
#                             best_video_url = f.get('url')
#                         elif resolution == "low" and best_video_url is None:
#                             best_video_url = f.get('url')
#                     elif f.get('acodec') and not f.get('vcodec'):  # صوت فقط
#                         if resolution == "audio" and best_audio_url is None:
#                             best_audio_url = f.get('url')

#                 # فتح رابط الفيديو أو الصوت
#                 if resolution == "audio" and best_audio_url:
#                     webbrowser.open(best_audio_url)
#                 elif (resolution == "high" or resolution == "low") and best_video_url:
#                     webbrowser.open(best_video_url)
#                 else:
#                     messagebox.showerror("خطأ", "لم يتم العثور على رابط فيديو أو صوت صالح.")

#             else:
#                 messagebox.showerror("خطأ", "لا توجد بيانات للفيديو.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# # واجهة المستخدم
# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()




# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}

#         # إعداد الخيارات بناءً على اختيار المستخدم
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             # استخراج جميع المعلومات المتاحة حول الفيديو
#             info = ydl.extract_info(url, download=False)

#             # تحقق من وجود التنسيقات
#             if 'formats' in info:
#                 formats = info['formats']
#                 best_video_url = None
#                 best_audio_url = None

#                 # التحقق من التنسيقات
#                 for f in formats:
#                     # البحث عن أفضل دقة فيديو وصوت (في حال الدقة العالية أو المنخفضة)
#                     if f.get('vcodec') and f.get('acodec'):
#                         if resolution == "high" and best_video_url is None:
#                             best_video_url = f.get('url')
#                         elif resolution == "low" and best_video_url is None:
#                             best_video_url = f.get('url')
#                     # إذا كان الصوت فقط
#                     elif f.get('acodec') and not f.get('vcodec'):
#                         if resolution == "audio" and best_audio_url is None:
#                             best_audio_url = f.get('url')

#                 # فتح الرابط المناسب
#                 if resolution == "audio" and best_audio_url:
#                     webbrowser.open(best_audio_url)
#                 elif (resolution == "high" or resolution == "low") and best_video_url:
#                     webbrowser.open(best_video_url)
#                 else:
#                     messagebox.showerror("خطأ", "لم يتم العثور على رابط فيديو أو صوت صالح.")

#             else:
#                 messagebox.showerror("خطأ", "لا توجد بيانات للفيديو.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# # واجهة المستخدم
# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# # إضافة الأزرار لاختيار الجودة
# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# # إضافة زر للخروج
# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()




# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}

#         # تحديد الخيارات بناءً على الدقة المطلوبة
#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo+bestaudio/best'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo+bestaudio/worst'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             # استخراج معلومات الفيديو
#             info = ydl.extract_info(url, download=False)

#             # عرض التنسيقات المتاحة في وحدة التحكم
#             if 'formats' in info:
#                 print("Available formats:")
#                 for f in info['formats']:
#                     print(f"Format ID: {f['format_id']}, Note: {f.get('format_note', 'N/A')}, URL: {f['url']}")

#             # محاولة تشغيل الفيديو/الصوت
#             if resolution in ["high", "low"]:
#                 video_url = info.get('url')
#                 if video_url:
#                     webbrowser.open(video_url)
#                 else:
#                     messagebox.showerror("خطأ", f"لم يتم العثور على فيديو بدقة {resolution}.")
#             elif resolution == "audio":
#                 audio_url = info.get('url')
#                 if audio_url:
#                     webbrowser.open(audio_url)
#                 else:
#                     messagebox.showerror("خطأ", "لم يتم العثور على صوت فقط.")
#             else:
#                 messagebox.showerror("خطأ", "اختيار غير صالح.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# # واجهة المستخدم
# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# # إضافة الأزرار لاختيار الجودة
# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# # إضافة زر للخروج
# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()






# import yt_dlp
# import webbrowser
# import re
# from tkinter import Tk, Entry, Button, Label, messagebox, Frame
# import os
# import subprocess

# def validate_url(url):
#     youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
#     return youtube_regex.match(url) is not None

# def play_video(resolution):
#     url = url_entry.get()
#     if not url:
#         messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
#         return

#     if not validate_url(url):
#         messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
#         return

#     try:
#         ydl_opts = {}

#         if resolution == "high":
#             ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'}
#         elif resolution == "low":
#             ydl_opts = {'format': 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]'}
#         elif resolution == "audio":
#             ydl_opts = {'format': 'bestaudio[ext=m4a]'}
#         else:
#             messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
#             return

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             video_url = None
#             audio_url = None

#             # إذا كانت الدقة عالية أو منخفضة، ابحث عن الفيديو والصوت
#             if resolution in ["high", "low"]:
#                 video_url = info.get('url')
#                 if 'formats' in info:
#                     for f in info['formats']:
#                         if f.get('vcodec') != 'none' and not video_url:
#                             video_url = f['url']
#                         if f.get('acodec') != 'none' and not audio_url:
#                             audio_url = f['url']
#             # إذا كان الصوت فقط
#             elif resolution == "audio":
#                 audio_url = info.get('url')

#             # تشغيل الفيديو والصوت باستخدام mpv أو فتح الرابط مباشرة
#             if resolution in ["high", "low"] and video_url and audio_url:
#                 # تحقق من وجود mpv لتشغيل الفيديو والصوت معًا
#                 if shutil.which("mpv"):
#                     subprocess.run(["mpv", video_url, "--audio-file=" + audio_url])
#                 else:
#                     webbrowser.open(video_url)
#             elif resolution == "audio" and audio_url:
#                 webbrowser.open(audio_url)
#             else:
#                 messagebox.showerror("خطأ", "لم يتم العثور على تنسيقات مناسبة للفيديو أو الصوت.")

#     except yt_dlp.utils.DownloadError as e:
#         messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
#     except Exception as e:
#         messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# # واجهة المستخدم
# window = Tk()
# window.title("مشغل الوسائط المتعددة")

# Label(window, text="أضف الرابط هنا").pack(pady=5)
# url_entry = Entry(window, width=50)
# url_entry.pack(pady=5)

# button_frame = Frame(window)
# button_frame.pack(pady=5)

# high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
# high_res_button.pack(side="left", padx=5)

# low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
# low_res_button.pack(side="left", padx=5)

# audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
# audio_button.pack(pady=5)

# exit_button = Button(window, text="خروج", command=window.quit)
# exit_button.pack(pady=5)

# window.mainloop()

import yt_dlp
import webbrowser
import re
from tkinter import Tk, Entry, Button, Label, messagebox, Frame
import os
import subprocess
import shutil  # تم إضافة هذا السطر

def validate_url(url):
    youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+')
    return youtube_regex.match(url) is not None

def play_video(resolution):
    url = url_entry.get()
    if not url:
        messagebox.showerror("خطأ", "يرجى إدخال رابط يوتيوب.")
        return

    if not validate_url(url):
        messagebox.showerror("خطأ", "الرابط المدخل غير صالح.")
        return

    try:
        ydl_opts = {}

        if resolution == "high":
            ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'}
        elif resolution == "low":
            ydl_opts = {'format': 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]'}
        elif resolution == "audio":
            ydl_opts = {'format': 'bestaudio[ext=m4a]'}
        else:
            messagebox.showerror("خطأ", "خيار الدقة غير صحيح.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = None
            audio_url = None

            if resolution in ["high", "low"]:
                video_url = info.get('url')
                if 'formats' in info:
                    for f in info['formats']:
                        if f.get('vcodec') != 'none' and not video_url:
                            video_url = f['url']
                        if f.get('acodec') != 'none' and not audio_url:
                            audio_url = f['url']
            elif resolution == "audio":
                audio_url = info.get('url')

            if resolution in ["high", "low"] and video_url and audio_url:
                if shutil.which("mpv"):
                    subprocess.run(["mpv", video_url, "--audio-file=" + audio_url])
                else:
                    webbrowser.open(video_url)
            elif resolution == "audio" and audio_url:
                webbrowser.open(audio_url)
            else:
                messagebox.showerror("خطأ", "لم يتم العثور على تنسيقات مناسبة للفيديو أو الصوت.")

    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("خطأ في التحميل", f"حدث خطأ أثناء معالجة الفيديو:\n{str(e)}")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ غير متوقع:\n{str(e)}")

# واجهة المستخدم
window = Tk()
window.title("مشغل الوسائط المتعددة")

Label(window, text="أضف الرابط هنا").pack(pady=5)
url_entry = Entry(window, width=50)
url_entry.pack(pady=5)

button_frame = Frame(window)
button_frame.pack(pady=5)

high_res_button = Button(button_frame, text="دقة عالية", command=lambda: play_video("high"))
high_res_button.pack(side="left", padx=5)

low_res_button = Button(button_frame, text="دقة منخفضة", command=lambda: play_video("low"))
low_res_button.pack(side="left", padx=5)

audio_button = Button(window, text="صوت فقط", command=lambda: play_video("audio"))
audio_button.pack(pady=5)

exit_button = Button(window, text="خروج", command=window.quit)
exit_button.pack(pady=5)

window.mainloop()


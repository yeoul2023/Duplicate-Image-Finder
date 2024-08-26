import difPy
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import send2trash


def run_search(folder_paths):
    # 이미지 검색 중 상태 표시
    progress_label.config(text="이미지 검색 중...")
    root.update_idletasks()

    # difPy를 사용하여 중복 이미지 검색
    dif = difPy.build(folder_paths)
    search = difPy.search(dif)

    # 검색 완료 상태 표시
    progress_label.config(text=f"검색 완료: {len(search.result)}개 중복 그룹, {len(search.lower_quality)}개 낮은 품질 이미지 발견.")
    root.update_idletasks()

    # 검색 결과를 표시
    show_results(search.result)


def browse_folders():
    folder_paths = []
    while True:
        folder_path = filedialog.askdirectory(title="폴더 선택")
        if folder_path:
            folder_paths.append(folder_path)
            if not messagebox.askyesno("추가 폴더", "다른 폴더를 추가로 선택하시겠습니까?"):
                break
        else:
            break
    if folder_paths:
        run_search(folder_paths)


def show_results(result):
    # 기존 결과 프레임 초기화
    for widget in result_frame.winfo_children():
        widget.destroy()

    result_canvas = tk.Canvas(result_frame)
    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_canvas.yview)
    scrollable_frame = ttk.Frame(result_canvas)

    scrollable_frame.bind("<Configure>", lambda e: result_canvas.configure(scrollregion=result_canvas.bbox("all")))
    result_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    result_canvas.configure(yscrollcommand=scrollbar.set)
    result_canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    groups = {}
    for primary_image, duplicates in result.items():
        all_images = [primary_image] + [dup[0] for dup in duplicates]
        if len(all_images) < 2:
            continue
        sorted_images = sorted(all_images, key=lambda x: os.path.getsize(x), reverse=True)
        group_frame = ttk.Frame(scrollable_frame)
        group_frame.pack(fill='x', pady=5)

        img_labels = []
        for image_path in sorted_images:
            img_frame = ttk.Frame(group_frame)
            img_frame.pack(side="left", padx=5, pady=5)

            img = Image.open(image_path)
            img.thumbnail((150, 150))
            img = ImageTk.PhotoImage(img)
            img_display = tk.Label(img_frame, image=img)
            img_display.image = img
            img_display.pack()

            delete_button = tk.Button(img_frame, text="X", command=lambda d=image_path, lbl=img_labels, gf=group_frame: confirm_delete(d, lbl, gf, groups))
            delete_button.place(x=130, y=0)

            img_labels.append((img_frame, image_path))

        groups[group_frame] = img_labels

        separator = ttk.Separator(scrollable_frame, orient='horizontal')
        separator.pack(fill='x')


def confirm_delete(image_path, img_labels, frame, groups):
    if messagebox.askyesno("삭제 확인", f"이미지 {image_path}를 정말 삭제하시겠습니까?"):
        try:
            send2trash.send2trash(image_path)

            for lbl, path in img_labels:
                if path == image_path:
                    lbl.destroy()
                    img_labels.remove((lbl, path))
                    break

            if len(img_labels) == 0:
                frame.destroy()
                del groups[frame]

            messagebox.showinfo("삭제 완료", f"이미지 {image_path}가 삭제되었습니다.")
        except Exception as e:
            messagebox.showerror("오류", f"이미지 삭제 중 오류가 발생했습니다: {e}")


def main():
    global root, result_frame, progress_label
    root = tk.Tk()
    root.title("Duplicate Image Finder")
    root.geometry("800x600")
    root.eval('tk::PlaceWindow . center')

    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10)

    select_button = ttk.Button(frame, text="폴더 선택", command=browse_folders)
    select_button.pack(pady=5)

    progress_label = ttk.Label(frame, text="")
    progress_label.pack(pady=5)

    result_frame = ttk.Frame(root)
    result_frame.pack(fill='both', expand=True)

    root.mainloop()


if __name__ == '__main__':
    main()

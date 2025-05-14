from pathlib import Path

# Текст для Reels у форматі .txt
reels_text = """✨ WordPress — це не лише для блогерів!
Це потужна CMS, яку ти можеш легко встановити локально — навіть через Docker або XAMPP.

⚙️ Кастомізуй її як завгодно: теми, плагіни, власний код — все під твоїм контролем.

🚀 Я почав серію постів, де ділюсь практичними порадами та прикладами.

🔗 Стартуй з першого кроку — лінк у першому коментарі!
"""

# Зберігаємо файл
file_path = Path("/home/shkodenko.t/prj/_github_podlom/php-dinos_python/_wordpress_reels_script.txt")
file_path.write_text(reels_text, encoding='utf-8')

print("The text was exported to file: " + file_path.name)

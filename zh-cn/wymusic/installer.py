�
    {��fK  �                   ��  � d dl Z d dlZdZdZde� d�ZddiZej        �                    d�  �        s ej        d�  �          e j	        ee�	�  �        j
        �                    �   �         �                    d
�  �        d         Z e j	        ee�	�  �        Z edd�  �        5 Ze�                    ej        �  �         ddd�  �         n# 1 swxY w Y    ed�  �         dS )�    Nz2https://byfuns.github.io/zh-cn/wymusic/version.txtg      �?z'https://byfuns.github.io/zh-cn/wymusic/z/main.pyz
User-Agentz�Mozilla/5.0 (Linux; Android 14; V2302A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/123.0.6312.118 Mobile Safari/537.36 VivoBrowser/21.0.60.0�MD)�url�headers�
�����z
MD/main.py�wbuJ   下载完成。你的下载命令为：

cd ~ && cd MD && python main.py

)�requests�os�check_new_version_url�version�downlaod_new_version_urlr   �path�exists�mkdir�get�text�strip�split�r�open�fp�write�content�print� �    �installer.py�<module>r      sT  �� ���� 	�	�	�	�L� �
��V�W�V�V�V� � �  t�u�� 
�w�~�~�d��� ��B�H�T�N�N�N� �(�,�0�'�
B�
B�
B�
G�
M�
M�
O�
O�
U�
U�VZ�
[�
[�\^�
_�� �H�L�-�w�?�?�?��	�T�,���� ���H�H�Q�Y����� � � � � � � � � � ���� � � � � ��V� W� W� W� W� Ws   �!C�C�C
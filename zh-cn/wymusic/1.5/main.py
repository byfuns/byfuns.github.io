�
    ���fk  �                   �   � d dl Z d dlZd dlmZ d dlZd dlZd dlZdZd� Zd� Zd� Z	d� Z
d� Zd	� Zd
� Zd� Zd� Zd� Zd� Zedk    r e�   �          dS dS )�    N)�BeautifulSoupg      �?c                  �b  � 	 ddi} t          j        d| t          ��  �        j        �                    �   �         �                    d�  �        d         }	 t          t          �  �        t          |�  �        k     }n	#  d}Y nxY w|�r"dt          |�  �        z  }t          j        || t          ��  �        j	        }d	D ]5}t          j        �                    |�  �        st          j        |�  �         �6t          d
d�  �        5 }t          dd�  �        5 }|�                    |�                    �   �         �  �         d d d �  �         n# 1 swxY w Y   d d d �  �         n# 1 swxY w Y   t          dd�  �        5 }|�                    |�  �         d d d �  �         d S # 1 swxY w Y   d S d S #  Y d S xY w)N�
User-Agentz�Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134z2https://byfuns.github.io/zh-cn/wymusic/version.txt��url�headers�verify�
�����Fz1https://byfuns.github.io/zh-cn/wymusic/%s/main.py��datazdata/backup/zdata/backup/main.py�wbzmain.py�rb)�requests�get�need_verify_or_not�text�strip�split�float�version�str�content�os�path�exists�mkdir�open�write�read)r   �new_version�is_old_version�version_url�new_version_file�i�fp�FPs           �-/storage/emulated/0/0/Products/MD/1.5/main.py�updater)      s�  � ���  ^�_�� 	��M�W^�gy�z�z�z��  	F�  	F�  	H�  	H�  	N�  	N��	� 	��	� 	�	#�"�7�^�^�e�K�.@�.@�@�N�N��	#�"�N�N�N����� 	+�M�PS�T_�P`�P`�`�K�'�|��W�Ug�h�h�h�p��-�  �  ���w�~�~�a�(�(�  ��H�Q�K�K�K�� �+�T�2�2� (�b��)�T�*�*� (�b��H�H�R�W�W�Y�Y�'�'�'�(� (� (� (� (� (� (� (� (� (� (���� (� (� (� (�(� (� (� (� (� (� (� (� (� (� (���� (� (� (� (�
 �i��&�&� +�"����)�*�*�*�+� +� +� +� +� +� +� +� +� +� +� +���� +� +� +� +� +� +�	+� 	+��������s�   �AF) �%A9 �8F) �9A?�=BF) � E�(E�9E�E		�	E�E		�E�F) �E � F) �#E �$F) �7F�F) �F�F) �!F�"F) �)F.c                 �J   � d}t          t          j        || �  �        �  �        S )Nz^(/[^/ ]*)+/$)�bool�re�match)r   �patterns     r(   �is_valid_linux_directoryr/   0   s!   � ��G�����$�'�'�(�(�(�    c                  �d  � t           j        �                    d�  �        r�t          dd�  �        5 } | �                    �   �         }d d d �  �         n# 1 swxY w Y   t          |�  �        r|S t          dd�  �        5 } | �                    d�  �         d d d �  �         n# 1 swxY w Y   t          d�  �         dS dD ]5}t           j        �                    |�  �        st          j        |�  �         �6t          dd�  �        5 } | �                    d�  �         d d d �  �         n# 1 swxY w Y   dS )N�data/config�r�wz/storage/emulated/0/MD/uJ   您设置的音乐保存目录异常，已设置为/storage/emulated/0/MD/r   )	r   r   r   r   r    r/   r   �printr   )r&   r   r%   s      r(   �get_music_save_dirr6   5   s�  � �	�w�~�~�m�$�$� )��-��%�%� 	���7�7�9�9�D�	� 	� 	� 	� 	� 	� 	� 	� 	� 	� 	���� 	� 	� 	� 	� $�D�)�)� 	-��K��m�S�)�)� 4�R����2�3�3�3�4� 4� 4� 4� 4� 4� 4� 4� 4� 4� 4���� 4� 4� 4� 4��^�_�_�_�,�,�)� 	� 	�A��7�>�>�!�$�$� ���������-��%�%� 	0���H�H�.�/�/�/�	0� 	0� 	0� 	0� 	0� 	0� 	0� 	0� 	0� 	0� 	0���� 	0� 	0� 	0� 	0�(�(s5   �A�A�A�=B�B#�&B#�D%�%D)�,D)c                 �   � t          j        dd| �  �        } t          j        dd| �  �        } t          j        dd| �  �        } | S )Nz[\\/*?:'<>|]�_z^\.� z\.$)r,   �sub)�ss    r(   �renamer<   J   s@   � �
����Q�'�'�A�
��v�r�1���A�
��v�r�1���A��Hr0   c                  �&   � da t          �   �          d S )NF)r   r)   � r0   r(   �not_need_verifyr?   T   s   � ���
�H�H�H�H�Hr0   c                 �t  � d| �                     d�  �        d         d d�         z   }ddi}t          j        ||t          ��  �        }t	          |j        d�  �        }t          |�                    d�  �        d	         �  �        �                     d
�  �        }|dd�         }d}|D ]}||z  }�t          |�  �        d         }||�	                    d�  �        dz   d �         �                     d�  �        d         }	|j
        �                    �   �         d d�         }
d|	z   |
�                    dd�  �        dz   fS )N�http�   i����r   �  Mozilla/5.0 (linux; android 8.1; eml-al00 build/huaweieml-al00; wv) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/53.0.2785.143 crosswalk/24.53.595.0 xweb/358 mmwebsdk/23 mobilesafari/537.36 micromessenger/6.7.2.1340 (0x2607023a) nettype/4g language/zh_cnr   zhtml.parser�script�����r
   r   r9   z@idzid=�   �&r   i����z.https://music.163.com/song/media/outer/url?id=�/u   、z.mp3)r   r   r   r   r   r   r   �find_all�eval�find�title�getText�replace)�
share_text�	share_urlr   �responds�soup�a�br%   r   �id�names              r(   � get_music_file_url_and_song_namerW   Z   s=  � ���)�)�&�1�1�!�4�T�c�T�:�:�I��  d�e�G��|�	�7�BT�U�U�U�H�����6�6�D� 	�D�M�M�(�#�#�B�'�(�(�.�.�t�4�4�A�	�!�B�$��A�
�A�� � ��	�Q����
�q�'�'�%�.�C�	�S�X�X�e�_�_�q� �!�!�	"�	(�	(��	-�	-�a�	0�B��:��������%�D�;�b�@�$�,�,�s�TY�BZ�BZ�]c�Bc�c�cr0   c                 �T  � ddi}t          j        | |t          ��  �        }t          ||z   d�  �        5 }|�                    |j        �  �        }d d d �  �         n# 1 swxY w Y   |dk    r(t          j        ||z   �  �         t          d�  �         d S t          |� d|� ��  �         d S )Nr   rC   r   r   i�  u9   [91m下载失败[0m，该歌曲需要VIP才能下载。u    已下载到)	r   r   r   r   r   r   r   �remover5   )r   rV   r   r   rQ   r&   �sizes          r(   �download_music_filer[   n   s�   � ��  d�e�G��|��W�=O�P�P�P�H�	�d�T�k�4�	 �	 � *�B��x�x��(�)�)��*� *� *� *� *� *� *� *� *� *� *���� *� *� *� *� �t�|�|�
�	�$��+�����O�P�P�P�P�P���*�*�D�*�*�+�+�+�+�+s   �A�A�"Ac                  �   � t          d�  �        } t          dd�  �        5 }|�                    | �  �         d d d �  �         d S # 1 swxY w Y   d S )NuI   设置目录
默认为：/storage/emulated0/MD/

请输入下载目录：r2   r4   )�inputr   r   )r   r&   s     r(   � function_seeting_save_mauic_pathr^   |   s�   � ��_�`�`�D�	�m�S�	!�	!� �R�
�������� � � � � � � � � � � ���� � � � � � s   �A�A�
Ac                 �b   � d� d� d� d� d�}|�                     | �  �        }|r |�   �          dS dS )Nc                  �   � t          �   �         S �N)r^   r>   r0   r(   �<lambda>z$is_other_functions.<locals>.<lambda>�   s   � �;�=�=� r0   c                  �    � t          d�  �        S )Nu�   [32m使用方法[0m
    直接到网易云，点击分享，点击 复制链接
    
    如：
    分享Nurko/Autrey的单曲《So Far Gone》: http://163cn.tv/vJz60UE (来自@网易云音乐)
    )r5   r>   r0   r(   rb   z$is_other_functions.<locals>.<lambda>�   s   � �� � 	� 	� r0   c                  �*   � t          t          �  �        S ra   )r5   r   r>   r0   r(   rb   z$is_other_functions.<locals>.<lambda>�   s   � �5��>�>� r0   c                  �   � t          �   �         S ra   )r?   r>   r0   r(   rb   z$is_other_functions.<locals>.<lambda>�   s   � ��(�(� r0   )�setting�helpr   �kfzTF)r   )�
user_input�actions�action_funcs      r(   �is_other_functionsrl   �   s\   � �=�=�	� 	� *�)�(�(�� �G� �+�+�j�)�)�K�� �������t��ur0   c                  �&  � t          �   �         } 	 t          d�  �        }|dk    rt          d�  �         d S t          |�  �        rnL|�                    d�  �        dk    r$t          |�  �        \  }}t          ||| �  �         nt          d�  �         ��)NTu   
分享的链接：r9   u(   已退出，输入help了解如何使用rA   r   u5   无法识别的命令，输入help了解如何使用
)r6   r]   r5   rl   rK   rW   r[   )�	song_pathri   �music_file_url�	song_names       r(   �downloadrq   �   s�   � �"�$�$�I�L��1�2�2�
� �����@�A�A�A��E��j�)�)� 	L���_�_�V�$�$��*�*�(H��(T�(T�%�N�I���	�9�E�E�E�E��J�K�K�K�Lr0   c                  �0  � da t          j        t          ��  �        } t          j        t          ��  �        }| �                    �   �          |�                    �   �          | �                    �   �          |�                    �   �          t          d�  �         d S )NT)�targetu   程序结束)r   �	threading�Threadr)   rq   �start�joinr5   )�update_thread�download_threads     r(   �mainrz   �   s�   � ����$�F�3�3�3�M��&�h�7�7�7�O� ������������ ������������	�.�����r0   �__main__)r   r   �bs4r   r,   rt   r   r)   r/   r6   r<   r?   rW   r[   r^   rl   rq   rz   �__name__r>   r0   r(   �<module>r~      s   �� 
�	�	�	� ���� � � � � � � 	�	�	�	� � � � � 	�	�	�	� ��� � �D)� )� )�
)� )� )�*� � �� � �d� d� d�(,� ,� ,�� � �� � �*L� L� L�$� � �$ �z����D�F�F�F�F�F� �r0   
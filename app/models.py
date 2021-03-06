from django.db import models
from django.core import validators


class Item(models.Model):

    OG_CHOICES = (
        (1, 'JR'),
        (2, '大手私鉄'),
        (3, '準大手私鉄'),
        (4, 'その他私鉄'),
        (5, '第三セクター')
    )
    OGName_CHICES = (
        (1, '-'),
        (2, 'JR北海道'),
        (3, 'JR東日本'),
        (4, 'JR東海'),
        (5, 'JR西日本'),
        (6, 'JR四国'),
        (7, 'JR九州'),
        (8, '東武鉄道'),
        (9, '京成電鉄'),
        (10, '西武鉄道'),
        (11, '京王電鉄'),
        (12, '小田急電鉄'),
        (13, '東京急行電鉄'),
        (14, '京浜急行電鉄'),
        (15, '東京メトロ'),
        (16, '相模鉄道'),
        (17, '名古屋鉄道'),
        (18, '近畿地方 '),
        (19, '近畿日本鉄道'),
        (20, '京阪電気鉄道'),
        (21, '阪急電鉄'),
        (22, '阪神電気鉄道'),
        (23, '南海電気鉄道'),
        (24, '西日本鉄道'),
        (25, '新京成電鉄'),
        (26, '北大阪急行電鉄'),
        (27, '泉北高速鉄道'),
        (28, '山陽電気鉄道'),
        (29, '神戸高速鉄道'),
        (30, '札幌市交通局'),
        (31, '函館市企業局交通部'),
        (32, '道南いさりび鉄道'),
        (33, '弘南鉄道'),
        (34, '津軽鉄道'),
        (35, '八戸臨海鉄道'),
        (36, '青い森鉄道 '),
        (37, '三陸鉄道'),
        (38, 'IGRいわて銀河鉄道'),
        (39, '仙台臨海鉄道'),
        (40, '仙台市交通局'),
        (41, '仙台空港鉄道'),
        (42, '由利高原鉄道'),
        (43, '秋田内陸縦貫鉄道'),
        (44, '山形鉄道'),
        (45, '阿武隈急行'),
        (46, '福島交通'),
        (47, '会津鉄道'),
        (48, 'ひたちなか海浜鉄道'),
        (49, '関東鉄道'),
        (50, '筑波観光鉄道'),
        (51, '鹿島臨海鉄道'),
        (52, '野岩鉄道'),
        (53, '真岡鐵道'),
        (54, '上信電鉄'),
        (55, '上毛電気鉄道'),
        (56, 'わたらせ渓谷鐵道'),
        (57, '秩父鉄道'),
        (58, '埼玉新都市交通'),
        (59, '埼玉高速鉄道'),
        (60, '流鉄'),
        (61, '銚子電気鉄道'),
        (62, '小湊鐵道'),
        (63, '北総鉄道'),
        (64, '山万'),
        (65, 'いすみ鉄道'),
        (66, '東葉高速鉄道'),
        (67, '芝山鉄道'),
        (68, '千葉都市モノレール'),
        (69, '舞浜リゾートライン'),
        (70, '千葉ニュータウン鉄道'),
        (71, '成田空港高速鉄道'),
        (72, '成田高速鉄道アクセス'),
        (73, '東京都交通局'),
        (74, '東京モノレール'),
        (75, 'ゆりかもめ'),
        (76, '東京臨海高速鉄道'),
        (77, '多摩都市モノレール'),
        (78, '首都圏新都市鉄道'),
        (79, '箱根登山鉄道'),
        (80, '伊豆箱根鉄道'),
        (81, '江ノ島電鉄'),
        (82, '横浜高速鉄道'),
        (83, '湘南モノレール'),
        (84, '横浜市交通局'),
        (85, '横浜シーサイドライン'),
        (86, '北越急行'),
        (87, 'えちごトキめき鉄道'),
        (88, '富山地方鉄道'),
        (89, 'あいの風とやま鉄道'),
        (90, '黒部峡谷鉄道'),
        (91, '万葉線'),
        (92, '富山ライトレール'),
        (93, '北陸鉄道'),
        (94, 'IRいしかわ鉄道'),
        (95, 'のと鉄道'),
        (96, '福井鉄道'),
        (97, 'えちぜん鉄道'),
        (98, '富士急行'),
        (99, 'アルピコ交通'),
        (100, '長野電鉄'),
        (101, '上田電鉄'),
        (102, 'しなの鉄道'),
        (103, '樽見鉄道'),
        (104, '明知鉄道'),
        (105, '長良川鉄道'),
        (106, '養老鉄道'),
        (107, '静岡鉄道'),
        (108, '大井川鐵道'),
        (109, '遠州鉄道'),
        (110, '岳南電車'),
        (111, '伊豆急行'),
        (112, '天竜浜名湖鉄道'),
        (113, '豊橋鉄道'),
        (114, '名古屋市交通局'),
        (115, '名古屋臨海高速鉄道'),
        (116, '愛知環状鉄道'),
        (117, '東海交通事業'),
        (118, '名古屋ガイドウェイバス'),
        (119, '愛知高速交通'),
        (120, '上飯田連絡線'),
        (121, '中部国際空港連絡鉄道'),
        (122, '三岐鉄道'),
        (123, '四日市あすなろう鉄道'),
        (124, '伊勢鉄道'),
        (125, '伊賀鉄道'),
        (126, '近江鉄道'),
        (127, '信楽高原鐵道'),
        (128, '京福電気鉄道'),
        (129, '京都市交通局'),
        (130, '叡山電鉄'),
        (131, '北近畿タンゴ鉄道'),
        (132, '嵯峨野観光鉄道'),
        (133, '水間鉄道'),
        (134, '大阪市高速電気軌道'),
        (135, '阪堺電気軌道'),
        (136, '大阪高速鉄道（大阪モノレール）'),
        (137, '大阪港トランスポートシステム'),
        (138, '神戸市交通局'),
        (139, '能勢電鉄'),
        (140, '神戸新交通'),
        (141, '北条鉄道'),
        (142, '神戸電鉄'),
        (143, '北神急行電鉄'),
        (144, '紀州鉄道'),
        (145, '和歌山電鐵'),
        (146, '若桜鉄道'),
        (147, '智頭急行'),
        (148, '一畑電車'),
        (149, '水島臨海鉄道'),
        (150, '井原鉄道'),
        (151, '岡山電気軌道'),
        (152, '広島電鉄'),
        (153, '広島高速交通'),
        (154, 'スカイレールサービス'),
        (155, '錦川鉄道'),
        (156, '阿佐海岸鉄道'),
        (157, '高松琴平電気鉄道'),
        (158, '伊予鉄道'),
        (159, '土佐くろしお鉄道'),
        (160, 'とさでん交通'),
        (161, '筑豊電気鉄道'),
        (162, '福岡市交通局'),
        (163, '甘木鉄道'),
        (164, '平成筑豊鉄道'),
        (165, '北九州高速鉄道'),
        (166, '松浦鉄道'),
        (167, '島原鉄道'),
        (168, '長崎電気軌道'),
        (169, '熊本電気鉄道'),
        (170, '南阿蘇鉄道'),
        (171, 'くま川鉄道'),
        (172, '熊本市交通局'),
        (173, '肥薩おれんじ鉄道'),
        (174, '鹿児島市交通局'),
        (175, '沖縄都市モノレール'),

    )

    station_name = models.CharField(
        verbose_name='駅名',
        max_length=200,
    )
    furigana = models.CharField(
        verbose_name='ふりがな',
        max_length=200,
    )
    Organization1_KindOfOG = models.IntegerField(
        verbose_name='会社種別',
        choices=OG_CHOICES,
        default=1
    )
    organization1 = models.IntegerField(
        verbose_name='鉄道会社1',
        choices=OGName_CHICES,
        default=3
    )
    organization2 = models.IntegerField(
        verbose_name='鉄道会社2',
        choices=OGName_CHICES,
        default=1
    )
    organization3 = models.IntegerField(
        verbose_name='鉄道会社3',
        choices=OGName_CHICES,
        default=1
    )
    organization4 = models.IntegerField(
        verbose_name='鉄道会社4',
        choices=OGName_CHICES,
        default=1
    )
    organization5 = models.IntegerField(
        verbose_name='鉄道会社5',
        choices=OGName_CHICES,
        default=1
    )
    organization6 = models.IntegerField(
        verbose_name='鉄道会社6',
        choices=OGName_CHICES,
        default=1
    )
    line1 = models.CharField(
        verbose_name='所属路線1',
        max_length=200,
    )
    line2 = models.CharField(
        verbose_name='所属路線2',
        max_length=200,
        blank=True,
        null=True,
    )
    line3 = models.CharField(
        verbose_name='所属路線3',
        max_length=200,
        blank=True,
        null=True,
    )
    line3 = models.CharField(
        verbose_name='所属路線3',
        max_length=200,
        blank=True,
        null=True,
    )
    line4 = models.CharField(
        verbose_name='所属路線4',
        max_length=200,
        blank=True,
        null=True,
    )
    line5 = models.CharField(
        verbose_name='所属路線5',
        max_length=200,
        blank=True,
        null=True,
    )
    line6 = models.CharField(
        verbose_name='所属路線6',
        max_length=200,
        blank=True,
        null=True,
    )
    line7 = models.CharField(
        verbose_name='所属路線7',
        max_length=200,
        blank=True,
        null=True,
    )
    line8 = models.CharField(
        verbose_name='所属路線8',
        max_length=200,
        blank=True,
        null=True,
    )
    line9 = models.CharField(
        verbose_name='所属路線9',
        max_length=200,
        blank=True,
        null=True,
    )
    prefectures = models.CharField(
        verbose_name='都道府県',
        max_length=200,
    )
    city = models.CharField(
        verbose_name='市区町村',
        max_length=200,
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        return self.station_name
        
    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
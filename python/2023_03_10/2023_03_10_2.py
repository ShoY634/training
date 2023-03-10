# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 月 = 6;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where NOT 月 = 6;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 降水量 < 100;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 降水量 > 200;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 最高気温 >= 30;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 最低気温 <= 0;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 月 in (3, 5, 7);

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 月 = any(3, 5, 7);

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 月 not in (3, 5, 7);

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where not 月 = any (3, 5, 7);

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 降水量 <= 100 AND 湿度 < 50;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 最低気温 < 5 OR 最高気温 > 35;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 湿度 BETWEEN 60 and 79;

# select 月, 降水量, 最高気温, 最低気温, 湿度
# from 気象観測
# where 降水量 IS NULL;

# select *
# from 都道府県
# where 都道府県名 like '%川';

# select *
# from 都道府県
# where 都道府県名 like '%島%';

# select *
# from 都道府県
# where 都道府県名 like '愛%';

# select *
# from 都道府県
# where 都道府県名 = 県庁所在地;

# select *
# from 都道府県
# where NOT 都道府県名 = 県庁所在地;

# select 学籍番号, 学生名, 法学, 経済学, 哲学, 情報理論, 外国語, 総合成績
# from 成績表;

# INSERT
# INTO 成績表(学籍番号, 学生名, 法学, 経済学, 哲学, 情報理論, 外国語)
# value('S001', '織田信長', 77, 55, 80, 75, 93) --コメント練習
# /* 他２人分は省略 */

# UPDATE 成績表
# set 法学 = 85, 哲学 = 67
# where 学籍番号 = 'S001';

# UPDATE 成績表
# set 外国語 = 81
# where 学籍番号 in ('A002', 'E003');

# UPDATE 成績表
# set 総合成績 = 'A'
# where 法学 >= 80 AND 経済学 >= 80 AND 哲学 >= 80 AND 情報理論 >= 80 AND 外国語 >= 80;

# UPDATE 成績表
# set 総合成績 = 'B'
# where (法学 >= 80 OR 外国語 >= 80) AND (経済学 >= 80 OR 哲学 >= 80) AND 総合成績 IS NULL;

# UPDATE 成績表
# set 総合成績 = 'D'
# where 法学 < 50 AND 経済学 < 50 AND 哲学 < 50 AND 情報理論 < 50 AND 外国語 < 50 AND 総合成績 IS NULL;

# UPDATE 成績表
# set 総合成績 = 'C'
# where 総合成績 IS NULL;

# DELETE from 成績表
# where 法学 = 0 OR 経済学 = 0 OR 哲学 = 0 OR 情報理論 = 0 OR 外国語 = 0;

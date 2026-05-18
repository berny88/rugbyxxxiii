-- CREATE TABLE GAME (
--     match_number INT PRIMARY KEY,
--     date_utc TIMESTAMP,
--     stage VARCHAR(50),
--     group_name VARCHAR(20),
--     team1_full VARCHAR(100),
--     team1_short VARCHAR(3),
--     team2_full VARCHAR(100),
--     team2_short VARCHAR(3),
--     functional_key VARCHAR(100)
-- );
-- Groupe A
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-MEX-RSA', '2026-06-11T19:00:00', 'MEX', 'RSA', 'Mexico', 'South Africa', NULL, NULL, 'group', 'Group A');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-KOR-CZE', '2026-06-12T02:00:00', 'KOR', 'CZE', 'Korea Republic', 'Czechia', NULL, NULL, 'group', 'Group A');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-CZE-RSA', '2026-06-18T16:00:00', 'CZE', 'RSA', 'Czechia', 'South Africa', NULL, NULL, 'group', 'Group A');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-MEX-KOR', '2026-06-19T01:00:00', 'MEX', 'KOR', 'Mexico', 'Korea Republic', NULL, NULL, 'group', 'Group A');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-RSA-KOR', '2026-06-25T01:00:00', 'RSA', 'KOR', 'South Africa', 'Korea Republic', NULL, NULL, 'group', 'Group A');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group A-CZE-MEX', '2026-06-25T01:00:00', 'CZE', 'MEX', 'Czechia', 'Mexico', NULL, NULL, 'group', 'Group A');

-- Groupe B
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-CAN-BIH', '2026-06-12T19:00:00', 'CAN', 'BIH', 'Canada', 'Bosnia and Herzegovina', NULL, NULL, 'group', 'Group B');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-QAT-SUI', '2026-06-13T19:00:00', 'QAT', 'CHE', 'Qatar', 'Switzerland', NULL, NULL, 'group', 'Group B');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-SUI-BIH', '2026-06-18T19:00:00', 'CHE', 'BIH', 'Switzerland', 'Bosnia and Herzegovina', NULL, NULL, 'group', 'Group B');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-CAN-QAT', '2026-06-18T22:00:00', 'CAN', 'QAT', 'Canada', 'Qatar', NULL, NULL, 'group', 'Group B');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-SUI-CAN', '2026-06-24T19:00:00', 'CHE', 'CAN', 'Switzerland', 'Canada', NULL, NULL, 'group', 'Group B');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group B-BIH-QAT', '2026-06-24T19:00:00', 'BIH', 'QAT', 'Bosnia and Herzegovina', 'Qatar', NULL, NULL, 'group', 'Group B');

-- Groupe C
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-BRA-MAR', '2026-06-13T22:00:00', 'BRA', 'MAR', 'Brazil', 'Morocco', NULL, NULL, 'group', 'Group C');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-HAI-SCO', '2026-06-14T01:00:00', 'HAI', 'SCO', 'Haiti', 'Scotland', NULL, NULL, 'group', 'Group C');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-BRA-HAI', '2026-06-20T00:30:00', 'BRA', 'HAI', 'Brazil', 'Haiti', NULL, NULL, 'group', 'Group C');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-SCO-MAR', '2026-06-19T22:00:00', 'SCO', 'MAR', 'Scotland', 'Morocco', NULL, NULL, 'group', 'Group C');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-SCO-BRA', '2026-06-24T22:00:00', 'SCO', 'BRA', 'Scotland', 'Brazil', NULL, NULL, 'group', 'Group C');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group C-MAR-HAI', '2026-06-24T22:00:00', 'MAR', 'HAI', 'Morocco', 'Haiti', NULL, NULL, 'group', 'Group C');

-- Groupe D
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-USA-PAR', '2026-06-13T01:00:00', 'USA', 'PAR', 'USA', 'Paraguay', NULL, NULL, 'group', 'Group D');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-AUS-TUR', '2026-06-14T04:00:00', 'AUS', 'TUR', 'Australia', 'Türkiye', NULL, NULL, 'group', 'Group D');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-USA-AUS', '2026-06-19T19:00:00', 'USA', 'AUS', 'USA', 'Australia', NULL, NULL, 'group', 'Group D');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-TUR-PAR', '2026-06-20T03:00:00', 'TUR', 'PAR', 'Türkiye', 'Paraguay', NULL, NULL, 'group', 'Group D');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-TUR-USA', '2026-06-26T02:00:00', 'TUR', 'USA', 'Türkiye', 'USA', NULL, NULL, 'group', 'Group D');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group D-PAR-AUS', '2026-06-26T02:00:00', 'PAR', 'AUS', 'Paraguay', 'Australia', NULL, NULL, 'group', 'Group D');

-- Groupe E
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-DEU-CUW', '2026-06-14T17:00:00', 'DEU', 'CUW', 'Germany', 'Curaçao', NULL, NULL, 'group', 'Group E');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-CIV-ECU', '2026-06-14T23:00:00', 'CIV', 'ECU', 'Côte d''Ivoire', 'Ecuador', NULL, NULL, 'group', 'Group E');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-DEU-CIV', '2026-06-20T20:00:00', 'DEU', 'CIV', 'Germany', 'Côte d''Ivoire', NULL, NULL, 'group', 'Group E');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-ECU-CUW', '2026-06-21T00:00:00', 'ECU', 'CUW', 'Ecuador', 'Curaçao', NULL, NULL, 'group', 'Group E');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-CUW-CIV', '2026-06-25T20:00:00', 'CUW', 'CIV', 'Curaçao', 'Côte d''Ivoire', NULL, NULL, 'group', 'Group E');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group E-ECU-GER', '2026-06-25T20:00:00', 'ECU', 'DEU', 'Ecuador', 'Germany', NULL, NULL, 'group', 'Group E');

-- Groupe F
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-NLD-JPN', '2026-06-14T20:00:00', 'NLD', 'JPN', 'Netherlands', 'Japan', NULL, NULL, 'group', 'Group F');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-SWE-TUN', '2026-06-15T02:00:00', 'SWE', 'TUN', 'Sweden', 'Tunisia', NULL, NULL, 'group', 'Group F');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-NLD-SWE', '2026-06-20T17:00:00', 'NLD', 'SWE', 'Netherlands', 'Sweden', NULL, NULL, 'group', 'Group F');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-TUN-JPN', '2026-06-21T04:00:00', 'TUN', 'JPN', 'Tunisia', 'Japan', NULL, NULL, 'group', 'Group F');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-JPN-SWE', '2026-06-25T23:00:00', 'JPN', 'SWE', 'Japan', 'Sweden', NULL, NULL, 'group', 'Group F');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group F-TUN-NED', '2026-06-25T23:00:00', 'TUN', 'NLD', 'Tunisia', 'Netherlands', NULL, NULL, 'group', 'Group F');

-- Groupe G
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-BEL-EGY', '2026-06-15T19:00:00', 'BEL', 'EGY', 'Belgium', 'Egypt', NULL, NULL, 'group', 'Group G');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-IRN-NZL', '2026-06-16T01:00:00', 'IRN', 'NZL', 'IR Iran', 'New Zealand', NULL, NULL, 'group', 'Group G');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-BEL-IRN', '2026-06-21T19:00:00', 'BEL', 'IRN', 'Belgium', 'IR Iran', NULL, NULL, 'group', 'Group G');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-NZL-EGY', '2026-06-22T01:00:00', 'NZL', 'EGY', 'New Zealand', 'Egypt', NULL, NULL, 'group', 'Group G');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-NZL-BEL', '2026-06-27T03:00:00', 'NZL', 'BEL', 'New Zealand', 'Belgium', NULL, NULL, 'group', 'Group G');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group G-EGY-IRN', '2026-06-27T03:00:00', 'EGY', 'IRN', 'Egypt', 'IR Iran', NULL, NULL, 'group', 'Group G');

-- Groupe H
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-ESP-CPV', '2026-06-15T16:00:00', 'ESP', 'CPV', 'Spain', 'Cabo Verde', NULL, NULL, 'group', 'Group H');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-KSA-URU', '2026-06-15T22:00:00', 'KSA', 'URU', 'Saudi Arabia', 'Uruguay', NULL, NULL, 'group', 'Group H');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-ESP-KSA', '2026-06-21T16:00:00', 'ESP', 'KSA', 'Spain', 'Saudi Arabia', NULL, NULL, 'group', 'Group H');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-URU-CPV', '2026-06-21T22:00:00', 'URU', 'CPV', 'Uruguay', 'Cabo Verde', NULL, NULL, 'group', 'Group H');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-CPV-KSA', '2026-06-27T00:00:00', 'CPV', 'KSA', 'Cabo Verde', 'Saudi Arabia', NULL, NULL, 'group', 'Group H');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group H-URU-ESP', '2026-06-27T00:00:00', 'URU', 'ESP', 'Uruguay', 'Spain', NULL, NULL, 'group', 'Group H');

-- Groupe I
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-FRA-SEN', '2026-06-16T19:00:00', 'FRA', 'SEN', 'France', 'Senegal', NULL, NULL, 'group', 'Group I');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-IRQ-NOR', '2026-06-16T22:00:00', 'IRQ', 'NOR', 'Iraq', 'Norway', NULL, NULL, 'group', 'Group I');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-NOR-SEN', '2026-06-23T00:00:00', 'NOR', 'SEN', 'Norway', 'Senegal', NULL, NULL, 'group', 'Group I');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-FRA-IRQ', '2026-06-22T21:00:00', 'FRA', 'IRQ', 'France', 'Iraq', NULL, NULL, 'group', 'Group I');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-NOR-FRA', '2026-06-26T19:00:00', 'NOR', 'FRA', 'Norway', 'France', NULL, NULL, 'group', 'Group I');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group I-SEN-IRQ', '2026-06-26T19:00:00', 'SEN', 'IRQ', 'Senegal', 'Iraq', NULL, NULL, 'group', 'Group I');

-- Groupe J
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-ARG-ALG', '2026-06-17T01:00:00', 'ARG', 'ALG', 'Argentina', 'Algeria', NULL, NULL, 'group', 'Group J');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-AUT-JOR', '2026-06-17T04:00:00', 'AUT', 'JOR', 'Austria', 'Jordan', NULL, NULL, 'group', 'Group J');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-ARG-AUT', '2026-06-22T17:00:00', 'ARG', 'AUT', 'Argentina', 'Austria', NULL, NULL, 'group', 'Group J');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-JOR-ALG', '2026-06-23T03:00:00', 'JOR', 'ALG', 'Jordan', 'Algeria', NULL, NULL, 'group', 'Group J');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-ALG-AUT', '2026-06-28T02:00:00', 'ALG', 'AUT', 'Algeria', 'Austria', NULL, NULL, 'group', 'Group J');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group J-JOR-ARG', '2026-06-28T02:00:00', 'JOR', 'ARG', 'Jordan', 'Argentina', NULL, NULL, 'group', 'Group J');

-- Groupe K
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-POR-COD', '2026-06-17T17:00:00', 'POR', 'COD', 'Portugal', 'Congo DR', NULL, NULL, 'group', 'Group K');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-UZB-COL', '2026-06-18T02:00:00', 'UZB', 'COL', 'Uzbekistan', 'Colombia', NULL, NULL, 'group', 'Group K');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-POR-UZB', '2026-06-23T17:00:00', 'POR', 'UZB', 'Portugal', 'Uzbekistan', NULL, NULL, 'group', 'Group K');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-COL-COD', '2026-06-24T02:00:00', 'COL', 'COD', 'Colombia', 'Congo DR', NULL, NULL, 'group', 'Group K');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-COL-POR', '2026-06-27T23:30:00', 'COL', 'POR', 'Colombia', 'Portugal', NULL, NULL, 'group', 'Group K');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group K-COD-UZB', '2026-06-27T23:30:00', 'COD', 'UZB', 'Congo DR', 'Uzbekistan', NULL, NULL, 'group', 'Group K');

-- Groupe L
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-GHA-PAN', '2026-06-17T23:00:00', 'GHA', 'PAN', 'Ghana', 'Panama', NULL, NULL, 'group', 'Group L');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-ENG-CRO', '2026-06-17T20:00:00', 'ENG', 'CRO', 'England', 'Croatia', NULL, NULL, 'group', 'Group L');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-ENG-GHA', '2026-06-23T20:00:00', 'ENG', 'GHA', 'England', 'Ghana', NULL, NULL, 'group', 'Group L');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-PAN-CRO', '2026-06-23T23:00:00', 'PAN', 'CRO', 'Panama', 'Croatia', NULL, NULL, 'group', 'Group L');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-PAN-ENG', '2026-06-27T21:00:00', 'PAN', 'ENG', 'Panama', 'England', NULL, NULL, 'group', 'Group L');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Group L-CRO-GHA', '2026-06-27T21:00:00', 'CRO', 'GHA', 'Croatia', 'Ghana', NULL, NULL, 'group', 'Group L');

INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W1-R2', '2026-06-28T19:00:00', 'W1', 'R2', 'Winner Match 1', 'Runner-up Match 2', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W2-R3', '2026-06-29T19:00:00', 'W2', 'R3', 'Winner Match 2', 'Runner-up Match 3', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W3-R4', '2026-06-29T20:30:00', 'W3', 'R4', 'Winner Match 3', 'Runner-up Match 4', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W4-R5', '2026-06-30T01:00:00', 'W4', 'R5', 'Winner Match 4', 'Runner-up Match 5', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W5-R6', '2026-06-30T17:00:00', 'W5', 'R6', 'Winner Match 5', 'Runner-up Match 6', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W6-R7', '2026-06-30T21:00:00', 'W6', 'R7', 'Winner Match 6', 'Runner-up Match 7', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W7-R8', '2026-07-01T01:00:00', 'W7', 'R8', 'Winner Match 7', 'Runner-up Match 8', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W8-R9', '2026-07-01T16:00:00', 'W8', 'R9', 'Winner Match 8', 'Runner-up Match 9', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W9-R10', '2026-07-01T20:00:00', 'W9', 'R10', 'Winner Match 9', 'Runner-up Match 10', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W10-R11', '2026-07-02T00:00:00', 'W10', 'R11', 'Winner Match 10', 'Runner-up Match 11', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W11-R12', '2026-07-02T19:00:00', 'W11', 'R12', 'Winner Match 11', 'Runner-up Match 12', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W12-R13', '2026-07-02T23:00:00', 'W12', 'R13', 'Winner Match 12', 'Runner-up Match 13', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W13-R14', '2026-07-03T03:00:00', 'W13', 'R14', 'Winner Match 13', 'Runner-up Match 14', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W14-R15', '2026-07-03T18:00:00', 'W14', 'R15', 'Winner Match 14', 'Runner-up Match 15', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W15-R16', '2026-07-03T22:00:00', 'W15', 'R16', 'Winner Match 15', 'Runner-up Match 16', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 32-W16-R17', '2026-07-04T01:30:00', 'W16', 'R17', 'Winner Match 16', 'Runner-up Match 17', NULL, NULL, 'KO', 'Round of 32');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W73-W74', '2026-07-04T17:00:00', 'W73', 'W74', 'Winner Match 73', 'Winner Match 74', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W74-W75', '2026-07-04T21:00:00', 'W74', 'W75', 'Winner Match 74', 'Winner Match 75', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W75-W76', '2026-07-05T20:00:00', 'W75', 'W76', 'Winner Match 75', 'Winner Match 76', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W76-W77', '2026-07-06T00:00:00', 'W76', 'W77', 'Winner Match 76', 'Winner Match 77', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W77-W78', '2026-07-06T19:00:00', 'W77', 'W78', 'Winner Match 77', 'Winner Match 78', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W78-W79', '2026-07-07T00:00:00', 'W78', 'W79', 'Winner Match 78', 'Winner Match 79', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W79-W80', '2026-07-07T16:00:00', 'W79', 'W80', 'Winner Match 79', 'Winner Match 80', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Round of 16-W80-W81', '2026-07-07T20:00:00', 'W80', 'W81', 'Winner Match 80', 'Winner Match 81', NULL, NULL, 'KO', 'Round of 16');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Quarter-final-W89-W90', '2026-07-09T20:00:00', 'W89', 'W90', 'Winner Match 89', 'Winner Match 90', NULL, NULL, 'KO', 'Quarter-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Quarter-final-W90-W91', '2026-07-10T19:00:00', 'W90', 'W91', 'Winner Match 90', 'Winner Match 91', NULL, NULL, 'KO', 'Quarter-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Quarter-final-W91-W92', '2026-07-11T21:00:00', 'W91', 'W92', 'Winner Match 91', 'Winner Match 92', NULL, NULL, 'KO', 'Quarter-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Quarter-final-W92-W93', '2026-07-12T01:00:00', 'W92', 'W93', 'Winner Match 92', 'Winner Match 93', NULL, NULL, 'KO', 'Quarter-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Semi-final-W97-W98', '2026-07-14T19:00:00', 'W97', 'W98', 'Winner Match 97', 'Winner Match 98', NULL, NULL, 'KO', 'Semi-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Semi-final-W98-W99', '2026-07-15T19:00:00', 'W98', 'W99', 'Winner Match 98', 'Winner Match 99', NULL, NULL, 'KO', 'Semi-final');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Third Place Play-off-LS1-LS2', '2026-07-18T21:00:00', 'LS1', 'LS2', 'Loser Semi-final 1', 'Loser Semi-final 2', NULL, NULL, 'KO', 'Third Place Play-off');
INSERT INTO GAME (key, date, teamA, teamB, libteamA, libteamB, resultA, resultB, category, categoryName) VALUES ('Final-WS1-WS2', '2026-07-19T19:00:00', 'WS1', 'WS2', 'Winner Semi-final 1', 'Winner Semi-final 2', NULL, NULL, 'KO', 'Final');
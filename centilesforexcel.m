function [HRchild, RRchild, HRbaby] = centilesforexcel(centilestr)
% [HRchild, RRchild, HRbaby] = centilesforexcel(centilestr)

childages = 0:1/12:18; % 0-18y in 1m steps
babyages = 0:2/365.25:62/365.25; % 0-62d in 2d steps

load kernelagecorrection;

[~, HRchild] = interpolateData(HRxhat, HRmhat.(centilestr), childages);
[~, RRchild] = interpolateData(BRxhat, BRmhat.(centilestr), childages);
[~, HRbaby] = interpolateData(HRxhat, HRmhat.(centilestr), babyages);

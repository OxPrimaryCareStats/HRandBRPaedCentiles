function [MHAT, X] = kernelregression(XI, YI, X, BW, WI, hmultiplier,p, minBW)
% kernel regression 
% 
% [M, X] = kernelregression(XI, YI, X, BW, WI, hmultiplier, p, minBW)
%
% XI and YI are data inputs (Nx1)  (required inputs)
% X are interpolation points for regression (1xM)
% BW are bandwidths associated with data (Nx1)
% WI are weights associated with data (Nx1)
% hmultiplier is the value of h (bandwidth) when BW = 1 (default=2)
% p is model order (default model order is 0)
% minBW is the minimum value of BW (to prevent problems with very low data
% bandwidths - default is eps)
%
% performs kernel regression using Gaussian kernels with variable
% bandwidths and weights
%
%
% Susannah Fleming  October 2009

% check inputs
if (nargin<2)
    error('sgf:input','at least 2 inputs required');
end
N = size(XI,1);
if (size(XI,2)~=1 || size(YI,1)~=N || size(YI,2)~=1)
    error('sgf:input', 'input sizes don''t match');
end
if (nargin>2)
    M=size(X,2);
    if(size(X,1)~=1), error('sgf:input','input sizes don''t match'); end
else
    M = 100;
    X = linspace(min(XI),max(XI),M);
end
if (nargin>3)
    if (size(BW,1)~=N || size(BW,2)~=1), error('sgf:input','input sizes don''t match'); end
else
    BW = ones(N,1);
end
if (nargin>4)
    if (size(WI,1)~=N || size(WI,2)~=1), error('sgf:input','input sizes don''t match'); end
else
    WI = ones(N,1);
end

% at some point, we may need to estimate a sensical value for h, but we'll do
% it by eye for now
if nargin<6, hmultiplier = 2; end

% currently only do Nadayara-Watson estimator
if nargin<7
    p=0;
    display('default Nadayara-Watson estimator');
end

% set minimum bandwidth
if nargin<8
    minBW =eps;
end
BW(BW<minBW) = minBW;

HI = BW*hmultiplier;


% matrices for doing calculation
XImat = repmat(XI,1,M);
YImat = repmat(YI,1,M);
Xmat = repmat(X,N,1);
HImat = repmat(HI,1,M);
WImat = repmat(WI,1,M);

% kernel (will be reused in calculation
Kh = (WImat./HImat) .* (1/sqrt(2*pi)) .* exp(-0.5 * (( (XImat-Xmat)./HImat).^2));

switch (p)
    case 0      
        numerat = sum(Kh .* YImat);
        denominat = sum(Kh);
        MHAT = numerat./denominat;
    case 1
        S0 = (1/N) * sum(Kh);
        S0mat = repmat(S0,N,1);
        S1 = (1/N) * sum( (XImat-Xmat) .* Kh);
        S1mat = repmat(S1,N,1);
        S2 = (1/N) * sum( ( (XImat-Xmat).^2) .* Kh);
        S2mat = repmat(S2,N,1);
        numerat = (S2mat - S1mat.*(XImat-Xmat)) .* Kh .* YImat;
        denominat = S2mat.*S0mat - S1mat.^2;
        MHAT = (1/N) * sum(numerat./denominat);         

    otherwise
        error('sgf:unsupported_model_order','only model orders 0 and 1 currently supported');
end


















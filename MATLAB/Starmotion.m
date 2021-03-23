spectra = importdata ("spectra.csv");
lambdaStart = importdata ("lambda_start.csv");
lambdaDelta = importdata ("lambda_delta.csv");
starNames = importdata ("star_names.csv");
lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c
nObs = size(spectra,1);
nSts = size (spectra,2);
lambdaEnd = lambdaStart + (nObs - 1) * lambdaDelta;
lambda = (lambdaStart : lambdaDelta : lambdaEnd)';
[sHa, idx] = min(spectra);
lambdaHa = lambda(idx);
z = (lambdaHa / lambdaPr) - 1;
speed = z * speedOfLight;
starInd = 1:1:nSts;
movaway = starNames(starInd (speed > 0));
fg1 = figure;
hold on
for nInd = 1:1:nSts
    
    if speed(nInd) < 0
    
        plot (lambda, spectra(:, nInd), "--", "LineWidth", 1)
        
    else
        plot (lambda, spectra(:, nInd), "LineWidth", 3)
    end
end
set(fg1, 'visible', 'on');
text (635, 3.35 * 10^-13, 'Полешко Анастасия, Б01-005');
xlabel('Длинна волны, нм')
ylabel (['Интенсивность, эрг/см^2/с/' , char(197)])
title ('Спектры звезд')
legend (starNames)
grid on
hold off
saveas(fg1, 'gr3.png')

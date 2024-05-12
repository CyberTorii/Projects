clear 

ci = clock;

Irgb = imread('Paysage.jpg');
Length = size(Irgb,1);
Width = size(Irgb,2);
I = rgb2gray(Irgb);
n=1; % Seuil de comptabilisation des pixels

% Filtrage moyenneur (lisseur) et normalisation

moyenneur = ones(3, 3) / 9;
I = conv2(I, moyenneur, 'same');

for C = 1:Length
  for L = 1:Width
    if I(C,L) > 255/2
      I(C,L)=255;
    else
      I(C,L)=0;
    end
  end
end

% Application du laplacien : differentielle finie centree

Edge = [Length, Width];

for C = 1:Length
    for L = 1:Width
        if (C <= n) || (L <= n) % Conditions aux limites de Dirichlet/Neumann
            Edge(C,L)=0;
        elseif (C >= Length-n) || (L >= Width-n) % Conditions aux limites de Dirichlet/Neumann
            Edge(C,L)=0;
        else           
            Dx2 = I(C+n,L) + I(C-n,L) - 2*I(C,L); % Approximation de la derivee seconde selon x
            Dy2 = I(C,L+n) + I(C,L-n) - 2*I(C,L); % Approximation de la derivee seconde selon y
            Dxy = I(C+n,L+n) + I(C-n,L-n) - 2*I(C,L); % Approximation de la derivee seconde selon x et y
            Dyx = I(C-n,L+n) + I(C+n,L-n) - 2*I(C,L); % Approximation de la derivee seconde selon y et x
            
            LP = Dx2 + Dy2 + Dxy + Dyx;    
            % Ou encore :         
            % LP = (I(C+n,L)+I(C-n,L)+I(C,L+n)+I(C,L-n)+I(C+n,L+n)+I(C-n,L-n)+I(C-n,L+n)+I(C+n,L-n))-8*I(C,L);        
            
            if abs(LP/(n^2)) > 0 % Si passage par 0 alors contour detecte
                Edge(C,L)=255;
            else
                Edge(C,L)=0;
            end
        end
    end
end

% Affiche les coutours sur l'image originale

Ic = Irgb;

for C = 1:Length
    for L = 1:Width
        if Edge(C,L) == 255
            Ic(C,L,1)=0;
            Ic(C,L,2)=255;
            Ic(C,L,3)=0;
        end
    end
end

subplot(1,3,1); % Affiche l'image originale
imshow(Ic)
axis image

subplot(1,3,2); % Affiche l'image apres le filtre moyenneur et normalisation
imagesc(I)
axis image

subplot(1,3,3); % Affiche l'image apres application du laplacien
imshow(Edge)
colormap(gray(2))
axis image

cf = clock;
t = cf-ci
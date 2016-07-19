from django.db import models

"""
DTS wowinex Datenaustausch

Auf dem Server von wowinex läuft ein Script als Job, der die
Daten aus wowinex mittels ODBC mit der Datenbank in DTS aktualisiert.
"""


class Unternehmen(models.Model):
    """
    Unternehmen - In wowinex Gibt es Mandanten, die mehrere Unternehmen haben koennen.

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage:
    SELECT PUB.Mandant.Unternehmen, PUB.Adresse.Name1 AS Name, PUB.Mandant.AdressNr
    FROM     PUB.Mandant, PUB.Adresse
    WHERE  PUB.Mandant.AdressNr = PUB.Adresse.AdressNr AND (PUB.Mandant.MandantNr = ?)
    """
    unternehmen = models.IntegerField(u'Unternehmen', blank=False, null=False)
    name = models.CharField(u'Name', max_length=150)
    adressenr = models.IntegerField(u'Adress Nr' )


class Wirtschaftseinheit(models.Model):
    """
    Wirtschaftseinheiten - oder auch ggf. Objekte genannt.

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage
    SELECT WE, Strasse, Postleitzahl, Ortname, Unternehmen, MandantNr
    FROM     PUB.Wirtschaftseinheit
    """
    we = models.IntegerField(u'WE', blank=False, null=False)
    strasse = models.CharField(u'Strasse', max_length=200, blank=True, null=True)
    plz = models.CharField(u'PLZ', max_length=7, blank=True, null=True)
    ort = models.CharField(u'Ortsname', max_length='200', blank=True, null=True)
    unternehmen = models.IntegerField(u'Unternehmen', blank=False, null=False)
    mandantnr = models.IntegerField(u'MandantNr', blank=False, null=False)


class Kreditor(models.Model):
    """
    Kreditor

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage (Achtung! Kreditor ist Unternehmen):
    SELECT PUB."Kreditor-Konto".Unternehmen, PUB."Kreditor-Konto".Kontonummer, PUB."Kreditor-Konto".Kontobezeichnung, PUB.Adresse.Name1, PUB.Adresse.Name2,
                  PUB.Adresse.Strasse, PUB.Adresse.PlzOrt, PUB.Adresse.PlzPostf, PUB.Adresse.Postfach, PUB.Adresse.Vorwahl1, PUB.Adresse.Telefon1, PUB.Adresse.Telefax,
                  PUB.Adresse.AdressNr, PUB.Adresse.Vermerk1, PUB.Adresse.Vermerk2, PUB.Adresse.Telefon2, PUB.Adresse.Vorwahl2, PUB.Adresse.VorwahlFax, PUB.Adresse.Ort,
                  PUB.Adresse.EMail, PUB.Adresse.VorwahlMobil, PUB.Adresse.TelefonMobil, PUB.Adresse.InternetURL, PUB.Adresse.PostfachStaat, PUB.Adresse.PostfachPLZ,
                  PUB.Adresse.PostfachOrt, PUB."Kreditor-Konto".MandantNr, PUB.Adresse.BriefAnrNr
    FROM     PUB."Kreditor-Konto", PUB.Adresse
    WHERE  PUB."Kreditor-Konto".Kontonummer = PUB.Adresse.AdressNr
    ORDER BY PUB."Kreditor-Konto".Kontobezeichnung

    Die AdresseNr steht im Bezug zu einer zentralen Adressentabelle in wowinex die sowohl
    Kreditoren als auch Debitoren und andere enthaelt.
    """
    kreditor = models.IntegerField(u'Kreditor', blank=False, null=False)
    adressnr = models.IntegerField(u'AdresseNr', blank=False, null=False)
    mandantnr = models.IntegerField(u'MandantNr', blank=False, null=False)
    briefanrede = models.IntegerField(u'BriefanredeNr', blank=False, null=False)


class Haus(models.Model):
    """
    Haus - Eine Wirtschaftseinheit kann mehrere Haeuser haben

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage:

    - Gerade nicht einsehbar, wird nachgereicht
    """
    #TODO: Haustabelle definieren

class NE(models.Model):
    """
    Nutzungseinheit (NE) - bzw. Wohnung - Ein Haus kann mehrere NE haben

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage:
    SELECT WohnNr
    FROM     PUB.xyWohnung
    WHERE  (MandantNr = 1) AND (WE = ?) AND (HausNr = ?) AND (Unternehmen = ?) AND (xyGeloescht = 0)
    """
    mandantnr = models.IntegerField(u'MandantNr', blank=False, null=False)
    unternehmen = models.IntegerField(u'Unternehmen', blank=False, null=False)
    wirtschaftseinheit = models.IntegerField(u'WE', blank=False, null=False)
    hausnr = models.IntegerField(u'HausNr', blank=False, null=False)
    nenr = models.IntegerField(u'NE_Nr', blank=False, null=False)


class Mieter(models.Model):
    """
    Mieter - (Debitor)

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage:

    SELECT PUB.xyMieter.AdressNr, PUB.xyMieter.WohnNr, PUB.Adresse.Name1, PUB.Adresse.Name2, PUB.Adresse.Ort, PUB.Adresse.Strasse, PUB.Adresse.EMail,
                  PUB.xyMieter.Folgenummer, PUB.xyMieter.Auszugsdatum, PUB.xyMieter.Einzugsdatum, PUB.Adresse.PlzOrt, PUB.Adresse.PlzPostf, PUB.Adresse.Postfach,
                  PUB.Adresse.Gebname, PUB.Adresse.Geschlecht, PUB.Adresse.VPName1, PUB.Adresse.VPName2, PUB.Adresse.Postleitzahl, PUB.Adresse.Ortname, PUB.xyMieter.HausNr,
                  PUB.xyMieter.MandantNr, PUB.xyMieter.Unternehmen, PUB.xyMieter.WE, PUB.xyMieter.Vertragadressnr
    FROM     PUB.xyMieter, PUB.Adresse
    WHERE  PUB.xyMieter.AdressNr = PUB.Adresse.AdressNr AND ((PUB.xyMieter.AdressNr <> 9999999) AND (PUB.xyMieter.xyBearbeiter <> '"Ess, Ess"') AND
                  (PUB.xyMieter.xyGeloescht <> - 1) AND (PUB.xyMieter.AbrechnenBeko <> '"N"') AND (PUB.xyMieter.Vertragadressnr <> 0) AND (PUB.Adresse.Name1 = ?) OR
                  (PUB.xyMieter.AdressNr = 1) AND (PUB.Adresse.Name1 = '2') AND (PUB.Adresse.Name2 = '3') AND (PUB.Adresse.Strasse = '4'))
    ORDER BY PUB.Adresse.Name1, PUB.Adresse.Name2, PUB.xyMieter.Folgenummer
    """

    mandantnr = models.IntegerField(u'MandantNr', blank=False, null=False)
    unternehmen = models.IntegerField(u'Unternehmen', blank=False, null=False)
    wirtschaftseinheit = models.IntegerField(u'WE', blank=False, null=False)
    hausnr = models.IntegerField(u'HausNr', blank=False, null=False)
    nenr = models.IntegerField(u'NE_nr', blank=False, null=False)
    adressenr = models.IntegerField(u'AdresseNr', blank=False, null=False)
    einzugdatum = models.DateTimeField(u'EinzugDatum')
    auszugdatum = models.DateTimeField(u'AuszugDatum', blank=True, null=True)
    folgenr = models.IntegerField(u'Folgenummer', blank=True, null=True)  # wievielte Mietverhaeltnis fuer NE
    vertragadressnr = models.IntegerField(u'Vertragspartner AdrNr', blank=True, null=True)


class Adresse(models.Model):
    """
    Adresse - Globale Adresstabelle für alles wie Debitor, Kreditor, Mieter etc.

    Daten werden von externem Script auf einem wowinex-server aktualisiert
    Der Benutzer fuer die Aktualisierung muss GruppenAdmin sein.

    Die Daten Stammen aus einer Abfrage:
    """

    #TODO: AdressenTabelle definieren